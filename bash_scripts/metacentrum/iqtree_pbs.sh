#!/bin/bash
#PBS -N IQT-ufb
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.12

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P1-7m_1-07G_L001-ds.67bbce8fcfb6439db0445956cac4f716/fire/ssu_tree-fungi/ver2_ufb'

#copy files to scratch
cp $datadir'/'*.aln $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
aln='fire_SSU-fungi.trimal_gt_0.8.aln'
# guide='guide_vps3-39'
# guide_tree=$guide'.treefile'
bb=1000
nm=5000

# iqtree -m TEST -bb $bb -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln
iqtree -m GTR+G -bb $bb -nm $nm -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln

# iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -pre $guide
# iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -b $bb -quiet -s $aln -ft $guide_tree #-wsr

#copy files back
rm $aln
cp * $datadir
