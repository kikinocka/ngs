#!/bin/bash
#PBS -N IQT-c20
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.12

datadir='/storage/brno3-cerit/home/kika/diplonema/ocdh/ver4'

#copy files to scratch
cp $datadir'/'*.aln $SCRATCHDIR
cp $datadir'/guide'* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
aln='ocdh.trimal_gt_0.8.aln'
guide='guide_ocdh'
guide_tree=$guide'.treefile'
bb=1000

# iqtree -m TEST -bb $bb -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln
# iqtree -m LG4X -b $bb -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln

# iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -pre $guide
iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s $aln -ft $guide_tree #-wsr

#copy files back
rm $aln
cp * $datadir
