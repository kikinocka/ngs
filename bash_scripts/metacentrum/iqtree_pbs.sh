#!/bin/bash
#PBS -N IQTree
#PBS -q default
#PBS -l select=1:ncpus=20:mem=30gb:scratch_local=10gb:os=debian9
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.8

datadir='/storage/brno3-cerit/home/kika/sags/concat/'

#copy files to scratch
cp $datadir'concat.aln' $SCRATCHDIR
# cp $datadir'guide_acsl_seqs.treefile' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
aln='concat.aln'
guide='guide_concat'
guide_tree=$guide'.treefile'
# guide_tree='guide_acsl_seqs.treefile'
bb=1000

# iqtree -s $aln -bb $bb -nt AUTO -ntmax $PBS_NUM_PPN -m TEST -quiet

iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -pre $guide
iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s $aln -ft $guide_tree

#copy files back
rm $aln
cp * $datadir
