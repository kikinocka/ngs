#!/bin/bash
#PBS -N IQTree
#PBS -q default
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb:os=debian9
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.8

datadir='/storage/brno3-cerit/home/kika/sags/ssus/eukaryotes/bs/'

#copy files to scratch
cp $datadir'ssus_eukaryotes.trimal_gt_0.8.aln' $SCRATCHDIR
# cp $datadir'guide_acsl_seqs.treefile' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
aln='ssus_eukaryotes.trimal_gt_0.8.aln'
# guide='guide_concat'
# guide_tree=$guide'.treefile'
bb=100

# iqtree -s $aln -bb $bb -nt AUTO -ntmax $PBS_NUM_PPN -m GTR+G -quiet
iqtree -s $aln -b $bb -nt AUTO -ntmax $PBS_NUM_PPN -m GTR+G -quiet

# iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -pre $guide
# iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s $aln -ft $guide_tree -wsr

#copy files back
rm $aln
cp * $datadir
