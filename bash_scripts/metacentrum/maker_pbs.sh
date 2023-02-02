#!/bin/bash
#PBS -N maker
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=5gb
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add maker-2.31.10

genome_dir='/storage/brno3-cerit/home/kika/blasto_comparative/final_genomes/'
datadir='/storage/brno3-cerit/home/kika/blasto_comparative/maker'

#copy files to scratch
cp $genome_dir'Omod_genome_final_masked.fa' $SCRATCHDIR
cp $datadir'/'* $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

mpirun -np $PBS_NUM_PPN maker

#copy files back
rm *.fa busco*fasta *ctl
cp -R * $datadir
