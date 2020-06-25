#!/bin/bash
#PBS -N IQT-LG4Xbs
#PBS -q default
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb:os=debian9
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.8

datadir='/storage/brno3-cerit/home/kika/sags/phylogenomics/concat_ver6_LG4X_bs/'

#copy files to scratch
cp $datadir'concat.aln' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
aln='concat.aln'
# guide='guide_concat'
# guide_tree=$guide'.treefile'
bb=1000

iqtree -s $aln -b $bb -nt AUTO -ntmax $PBS_NUM_PPN -m LG4X -quiet -wsr
# iqtree -s $aln -bb $bb -nt AUTO -ntmax $PBS_NUM_PPN -m LG4X -quiet -wsr

# iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -pre $guide
# iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s $aln -ft $guide_tree #-wsr

#copy files back
rm $aln
cp * $datadir
