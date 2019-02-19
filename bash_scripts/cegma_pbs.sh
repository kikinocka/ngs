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

genome_dir='/auto/brno3-cerit/nfs4/home/kika/pelomyxa/genome_assembly/'

#copy file to scratch
cd $genome_dir
cp pelomyxa_clean.fa $SCRATCHDIR

genome='pelomyxa_clean.fa'

cd $SCRATCHDIR
cegma -o pelo_spades_cegma -T $PBS_NUM_PPN -g $genome

cp pelo_spades_cegma* $genome_dir
