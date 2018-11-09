#!/bin/bash
#PBS -N CEGMA
#PBS -l select=1:ncpus=5:mem=10gb:scratch_local=100gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add cegma-2.5
module add blast+-2.2.29

genome_dir='/storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/deep_hiseq/p5/'

#copy file to scratch
cd $genome_dir
cp scaffolds.fasta $SCRATCHDIR

genome='scaffolds.fasta'

cd $SCRATCHDIR
cegma -o p5_cegma -T $PBS_NUM_PPN -g $genome

cp p5_cegma* $genome_dir
