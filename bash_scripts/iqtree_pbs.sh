#!/bin/sh
#PBS -N IQTree
#PBS -q default
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=30gb:os=debian9
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.8

datadir='/storage/brno3-cerit/home/kika/catalase/'

#copy files to scratch
cp $datadir'catalase_trimal_automated1.aln' $SCRATCHDIR

#compute on scratch
aln='catalase_trimal_automated1.aln'
bb=1000

iqtree -s $aln -bb $bb -nt AUTO -m TEST

#copy files back
rm $aln
cp * $datadir
