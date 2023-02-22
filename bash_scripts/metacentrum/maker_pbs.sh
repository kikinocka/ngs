#!/bin/bash
#PBS -N maker
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=168:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module add maker-2.31.10
module add augustus-3.4.0
module load genemark-4.68
module add snap-korf/2021-11-04-gcc-10.2.1-5kjikze


genome_dir='/storage/brno3-cerit/home/kika/blasto_comparative/final_genomes/'
repeat_dir='/storage/brno3-cerit/home/kika/blasto_comparative/genome_repeats/'
rna_dir='/storage/brno3-cerit/home/kika/blasto_comparative/RNAs/'
datadir='/storage/brno3-cerit/home/kika/blasto_comparative/maker'

#copy files to scratch
cp $genome_dir'Omod_genome_final_masked.fa' $SCRATCHDIR
cp $repeat_dir'Omod_genome-families.fa' $SCRATCHDIR
cp $rna_dir'Omod_'* $SCRATCHDIR
cp -r $datadir'/'* $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR
mkdir $SCRATCHDIR/augustus_configs
cp -r $AUGUSTUS_CONFIG_PATH/* $SCRATCHDIR/augustus_configs/
export AUGUSTUS_CONFIG_PATH=$SCRATCHDIR/augustus_configs
 
mkdir tmp
mpirun maker -TMP $SCRATCHDIR/tmp

#copy files back
rm -r 'Omod_genome_final_masked.fa' 'Omod_genome-families.fa' *_RNAs.* busco*fasta augustus_configs
cp -R * $datadir
