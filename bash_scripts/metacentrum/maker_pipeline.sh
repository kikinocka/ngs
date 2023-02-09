#!/bin/bash

#RUN IN YOUR FOLDER
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module add snap-korf/2021-11-04-gcc-10.2.1-5kjikze
module add maker-2.31.10


#Create configuration files
maker -CTL
	#creates maker_bopts.ctl, maker_evm.ctl, maker_exe.ctl, maker_opts.ctl

#Modify options in maker_opts.ctl
genome=Omod_genome_final_masked.fa
protein=busco-eugl_plus_swissprot-tryps.fasta #more files can be provided, sep. by comma
protein2genome=1
model_org= #Leave empty to skip TE masking for the training
split_hit=0 #length for the splitting of hits (expected max intron size for evidence alignments) – in v2.31.10
min_intron=0 #minimum intron length (used for alignment polishing) - not available in v2.31.10
single_exon=1 #consider single exon EST evidence when generating annotations, 1 = yes, 0 = no
single_length=0 #min length required for single exon ESTs if 'single_exon is enabled'
min_protein=30 #require at least this many amino acids in predicted proteins


#run MAKER in SCRATCHDIR
qsub maker_pbs.sh


#Get the GFF with the annotation
gff3_merge -d Omod_genome_final_masked.maker.output/Omod_genome_final_masked_master_datastore_index.log
	#creates Omod_genome_final_masked.all.gff
	#it will contain several false positives that will be filtered out from the training with the following below


#Check amount of genes with introns (>1 exon)
grep -i "mrna-1:2" Omod_genome_final_masked.all.gff

#Check AED of predictions
export LC_ALL=C

grep AED Omod_genome_final_masked.all.gff | cut -f1,9 | sed 's/;/\t/g' | cut -f1,2,5 | sort -k3

#Check amount of predictions with AED <= 0.25
grep AED Omod_genome_final_masked.all.gff | cut -f1,9 | sed 's/;/\t/g' | cut -f1,2,5 | sort -k3 | sed 's/=/\t/g' | awk '{if ($5<=0.25) {print}}'
#Check amount of predictions with AED > 0.25
grep AED Omod_genome_final_masked.all.gff | cut -f1,9 | sed 's/;/\t/g' | cut -f1,2,5 | sort -k3 | sed 's/=/\t/g' | awk '{if ($5>0.25) {print}}'


#Run maker2zff to get the files needed to train SNAP (only AED > 0.25 and length > 50)
maker2zff -x 0.25 -l 50 Omod_genome_final_masked.all.gff 
	#– produced empty genome.ann and genome.dna files
remove_AED.py
	#AED > 0.25 removed manually by 
	#then no filtering used, proceeded with next command using Omod_genome_final_masked.all_upd.gff file
maker2zff -n Omod_genome_final_masked.all_upd.gff
	#creates genome.ann (the ZFF format file) and genome.dna (a FASTA file the coordinates can be referenced against). These will be used to train SNAP.)
	#genome.ann and genome.dna contain information about the gene sequences (such as exons and introns) as well as the actual DNA sequence


#Run fathom, forge and hmm-assembler from SNAP to get the training models
fathom -categorize 1000 genome.ann genome.dna
	#collect the training sequences and annotations, plus 1000 surrounding bp for training. Creates alt.ann alt.dna err.ann err.dna olp.ann olp.dna uni.ann uni.dna wrn.ann wrn.dna.
fathom -export 1000 -plus uni.ann uni.dna
	#capture the CDS and the protein sequence of each model. Creates export.aa export.ann export.dna export.tx
forge export.ann export.dna
	#Creates UTR3 and UTR5 files, as well start, stop, polyA, intron, donor, transitions, etc
hmm-assembler.pl Omod_train1 . > Omod_train1_snap_r00.hmm
	#finally uses those captured segments to produce the HMM that is added to maker_opts.ctl file


#Modify options in maker_opts.ctl for SNAP training with HMMs
est2genome=0
protein2genome=0
snaphmm=Omod_train1_snap_r00.hmm


#run MAKER in SCRATCHDIR
qsub maker_pbs.sh


#Get the GFF with the annotation
gff3_merge -d Omod_genome_final_masked.maker.output/Omod_genome_final_masked_master_datastore_index.log
	#this will overwritte Omod_genome_final_masked.all.gff, so first renamed to Omod_genome_final_masked.all1.gff

