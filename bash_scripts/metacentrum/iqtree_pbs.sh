#!/bin/bash
#PBS -N IQT
#PBS -q default
#PBS -l select=1:ncpus=15:mem=15:scratch_local=1gb:os=debian9
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.8

datadir='/storage/brno3-cerit/home/kika/trafficking/RABs/ver3'

#copy files to scratch
cp $datadir'/'* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
aln='rabs.trimal_gt_0.8.aln'
guide='guide_rabs'
guide_tree=$guide'.treefile'
bb=1000

# iqtree -s $aln -b $bb -nt AUTO -ntmax $PBS_NUM_PPN -m TEST -quiet -wsr
# iqtree -s $aln -b $bb -nt AUTO -ntmax $PBS_NUM_PPN -m LG4X -quiet -wsr

iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -pre $guide
iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s $aln -ft $guide_tree #-wsr

#copy files back
rm $aln
cp * $datadir
