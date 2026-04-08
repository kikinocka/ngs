#!/bin/bash
#PBS -N braker4
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module load augustus

#setting augustus config file environment variable
mkdir $SCRATCHDIR/augustus_configs
cp -r $AUGUSTUS_CONFIG_PATH/* $SCRATCHDIR/augustus_configs/
export AUGUSTUS_CONFIG_PATH=$SCRATCHDIR/augustus_configs


genome_dir='/storage/brno12-cerit/home/kika/blastocystis/ASM2924153v1/'
# map_dir='/storage/brno12-cerit/home/kika/trypanosoma_boissoni/hisat2/'
# rna_dir='/storage/brno12-cerit/home/kika/trypanosoma_boissoni/RNA_reads/'
prot_dir='/storage/brno12-cerit/home/kika/databases/'

#copy files to scratch
cp $genome_dir'GCA_029241535.1_ASM2924153v1_genomic.fna' $SCRATCHDIR
# cp $map_dir'Tboi_ht2_sorted.pass.bam' $SCRATCHDIR
cp $prot_dir'Stramenopiles.fa' $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

genome='GCA_029241535.1_ASM2924153v1_genomic.fna'
# bam='Tboi_ht2_sorted.pass.bam'
prot='Stramenopiles.fa'
name='blastocystis_CHMP1T17'

singularity exec /cvmfs/singularity.metacentrum.cz/Braker/braker3-v.3.0.8.sif braker.pl \
	--genome=$genome \
	--prot_seq=$prot \
	--species=$name \
	--workingdir=$SCRATCHDIR \
	--threads $PBS_NUM_PPN \
	--gff3

# --bam=rnaseq.bam
# --rnaseq_sets_ids=SRR1111,SRR1115
# --rnaseq_sets_dir=/path/to/rna_dir1


#copy files back
rm $genome $prot #$bam *fq.gz
rm -r augustus_configs
cp -r * $genome_dir'braker/' && clean_scratch
