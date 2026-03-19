#!/bin/bash
#PBS -N eukan
#PBS -l select=1:ncpus=20:mem=200gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

genome_dir='/storage/brno12-cerit/home/kika/paratrimastix/'
# read_dir='/storage/brno12-cerit/home/kika/paratrimastix/RNA_reads'
prot_dir='/storage/brno12-cerit/home/kika/databases/'
transc_dir='/storage/brno12-cerit/home/kika/paratrimastix/eukan/transcriptome_flye/'

#copy files to scratch
cp $genome_dir'flye_assembly.pilon.remove_contaminants.260210.fasta' $SCRATCHDIR
# cp $read_dir'/SRR33713718'*fq.gz $SCRATCHDIR
cp $prot_dir'Eukaryota_odb12.fa' $SCRATCHDIR
cp $transc_dir'nr_transcripts.'* $SCRATCHDIR
cp $transc_dir'hints_rnaseq.gff' $SCRATCHDIR
cp $transc_dir'flye_assembly.sqlite' $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

# #1) Prepare RNA-seq data to produce input files for the main pipeline. mem=1000GB
# genome='flye_assembly.pilon.remove_contaminants.260210.fasta'
# fwd='SRR33713718_trimmed_1.fq.gz'
# rev='SRR33713718_trimmed_2.fq.gz'
# # sg1='SRR651041_trimmed.fq.gz'
# # sg2='SRR651098_trimmed.fq.gz'
# max_intron=10000

# singularity exec /cvmfs/singularity.metacentrum.cz/Eukan/eukan.sif /bin/bash /opt/eukan/transcriptome_assembly.sh \
#     -l $fwd -r $rev \
#     -g $genome \
#     -M $max_intron \
#     -A -T -P \
#     -S FR \
#     -n $PBS_NUM_PPN
# #-s $sg1,$sg2 

#2) Main Eukan pipeline.
genome='flye_assembly.pilon.remove_contaminants.260210.fasta'
proteins='Eukaryota_odb12.fa'
transc_fasta='nr_transcripts.fasta'
transc_gff='nr_transcripts.gff3'
hints='hints_rnaseq.gff'
pasa='flye_assembly.sqlite'

singularity exec /cvmfs/singularity.metacentrum.cz/Eukan/eukan-1.0.0zs.sif \
	cp -r /opt/Augustus/config $SCRATCHDIR/augustus_config
singularity exec -H /storage/brno12-cerit/home/kika --env AUGUSTUS_CONFIG_PATH=$SCRATCHDIR/augustus_config \
	/cvmfs/singularity.metacentrum.cz/Eukan/eukan-1.0.0zs.sif eukan \
	-g $genome \
	-p $proteins \
	-tf $transc_fasta \
	-tg $transc_gff \
	-r $hints \
	--utrs $pasa \
	--numcpu $PBS_NUM_PPN \
	--protist

#copy files back
# rm $genome $fwd $rev $sg1 $sg2
mv augustus_config/species/flye_assembly.* .
rm -r augustus_config
rm $genome $proteins $transc_fasta $transc_gff $hints $pasa 
cp -r * $genome_dir'eukan/eukaryotes/' && clean_scratch
