#!/bin/bash
#PBS -N IQT-cox1
#PBS -q default
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb:os=debian9
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.8

datadir='/storage/brno3-cerit/home/kika/sags/cox1/'

#copy files to scratch
cp $datadir'cox1_final.aln' $SCRATCHDIR
# cp $datadir'guide_acsl_seqs.treefile' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
aln='cox1_final.aln'
# guide='guide_concat'
# guide_tree=$guide'.treefile'
bb=100

# iqtree -s $aln -bb $bb -nt AUTO -ntmax $PBS_NUM_PPN -m GTR+G -quiet
iqtree -s $aln -b $bb -nt AUTO -ntmax $PBS_NUM_PPN -m TEST -quiet -wsr

# iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -pre $guide
# iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s $aln -ft $guide_tree

#copy files back
rm $aln
cp * $datadir
