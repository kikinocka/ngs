#!/bin/bash
#PBS -N eukan-kin
#PBS -l select=1:ncpus=20:mem=200gb:scratch_local=50gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

genome_dir='/storage/brno12-cerit/home/kika/trypanosoma_boissoni/'
# read_dir='/storage/brno12-cerit/home/kika/trypanosoma_boissoni/RNA_reads/'
transc_dir='/storage/brno12-cerit/home/kika/trypanosoma_boissoni/eukan/transcriptome/'
prot_dir='/storage/brno12-cerit/home/kika/databases/'

#copy files to scratch
cp $genome_dir'Tboi_GCA_030849725.fna' $SCRATCHDIR
# cp $read_dir'Tboi_trimmed50_'*fq.gz $SCRATCHDIR
cp $transc_dir'nr_transcripts.'* $SCRATCHDIR
cp $transc_dir'hints_rnaseq.gff' $SCRATCHDIR
cp $transc_dir'Tboi_GCA_030849725.sqlite' $SCRATCHDIR
cp $prot_dir'kinetoplastids.faa' $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

# #1) Prepare RNA-seq data to produce input files for the main pipeline. mem=1000GB
# genome='Tboi_GCA_030849725.fna'
# fwd='Tboi_trimmed50_1.fq.gz'
# rev='Tboi_trimmed50_2.fq.gz'
# # sg1='SRR651041_trimmed.fq.gz'
# # sg2='SRR651098_trimmed.fq.gz'
# max_intron=0

# singularity exec /cvmfs/singularity.metacentrum.cz/Eukan/eukan-1.0.0zs.sif \
# 	/bin/bash /opt/eukan/transcriptome_assembly.sh \
#     -l $fwd -r $rev \
#     -g $genome \
#     -M $max_intron \
#     -A -T -P \
#     -S FR \
#     -n $PBS_NUM_PPN
# #-s $sg1,$sg2 

#2) Main Eukan pipeline.
genome='Tboi_GCA_030849725.fna'
transc_fasta='nr_transcripts.fasta'
transc_gff='nr_transcripts.gff3'
hints='hints_rnaseq.gff'
pasa='Tboi_GCA_030849725.sqlite'
proteins='kinetoplastids.faa'

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


# #copy files back
# rm $genome $fwd $rev
# cp -r * $genome_dir'eukan/transcriptome/' && clean_scratch

mv augustus_config/species/flye_assembly.* .
rm -r augustus_config
rm $genome $proteins $transc_fasta $transc_gff $hints $pasa 
cp -r * $genome_dir'eukan/kinetoplastids/' && clean_scratch
