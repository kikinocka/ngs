#!/bin/bash
#PBS -N braker
#PBS -l select=1:ncpus=20:mem=70gb:scratch_local=50gb
#PBS -l walltime=2:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module load augustus

#setting augustus config file environment variable
mkdir $SCRATCHDIR/augustus_configs
cp -r $AUGUSTUS_CONFIG_PATH/* $SCRATCHDIR/augustus_configs/
export AUGUSTUS_CONFIG_PATH=$SCRATCHDIR/augustus_configs


genome_dir='/storage/brno12-cerit/home/kika/paratrimastix/'
rna_dir='/storage/brno12-cerit/home/kika/paratrimastix/hisat2/'
prot_dir='/storage/brno12-cerit/home/kika/databases/'

#copy files to scratch
cp $genome_dir'PaPyr_JAPMOS01.fna' $SCRATCHDIR
# cp $rna_dir'PaPyr_ht2_sorted.bam' $SCRATCHDIR
cp $prot_dir'metamonads.faa' $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

genome=PaPyr_JAPMOS01.fna
# rna_ids=SRR651098,SRR651041,SRR33713718
# bam=PaPyr_ht2_sorted.bam
prot=metamonads.faa
name='paratrimastix_pyriformis'

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
rm $genome $prot $bam
rm -r augustus_configs
cp -r * $genome_dir'braker'
