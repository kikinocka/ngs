#!/bin/bash
#PBS -N IQT-test
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.8

datadir='/storage/brno3-cerit/home/kika/anaeramoeba'

#copy files to scratch
cp $datadir'/'* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
aln='hops_corvet.trimal_gt_0.8.aln'
# guide='guide_rabs.trimal_gt_0.8.aln'
# guide_tree=$guide'.treefile'
bb=1000
nm=2000

iqtree -s $aln -bb $bb -nt AUTO -ntmax $PBS_NUM_PPN -m TEST -quiet #-wsr
# iqtree -s $aln -bb $bb -nt AUTO -ntmax $PBS_NUM_PPN -m LG4X -quiet #-wsr

# iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -pre $guide
# iqtree -m LG+C60+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -nm $nm -quiet -s $aln -ft $guide_tree #-wsr

#copy files back
rm $aln
cp * $datadir
