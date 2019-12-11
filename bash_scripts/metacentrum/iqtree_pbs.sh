#!/bin/bash
#PBS -N IQTree
#PBS -q default
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=30gb:os=debian9
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.8

datadir='/storage/brno3-cerit/home/kika/elonga_bct_genomes/tree/'

#copy files to scratch
cp $datadir'SDR_a4_trimal_0.75.aln' $SCRATCHDIR
cp $datadir'guide_SDR_a4.treefile' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
aln='SDR_a4_trimal_0.75.aln'
guide='guide_SDR_a4'
guide_tree=$guide'.treefile'
bb=1000

# iqtree -s $aln -bb $bb -nt AUTO -ntmax $PBS_NUM_PPN -m TEST -quiet

# iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -pre $guide
iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s $aln -ft $guide_tree

#copy files back
rm $aln
cp * $datadir
