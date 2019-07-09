#!/bin/sh
#PBS -N IQTree
#PBS -q default
#PBS -l select=1:ncpus=10:mem=2gb:scratch_local=30gb:os=debian9
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.8

datadir='/storage/brno3-cerit/home/kika/paramylon/synthase/'

#copy files to scratch
cp $datadir'glucane_synthase_trimal_automated1.aln' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
aln='glucane_synthase_trimal_automated1.aln'
guide='guide_glucane_synthase'
guide_tree=$guide'.treefile'
bb=1000

# iqtree -s $aln -bb $bb -nt AUTO -m TEST

iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -pre $guide
iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s $aln -ft $guide_tree

#copy files back
rm $aln
cp * $datadir
