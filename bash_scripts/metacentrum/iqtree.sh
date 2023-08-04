#!/bin/bash
#PBS -N IQT
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.12
# source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
# module load iqtree

datadir='/storage/brno3-cerit/home/kika/p57/amastins/ver3/'

#copy files to scratch
# cp $datadir'/'*.aln $SCRATCHDIR
cp $datadir'amastins.trimal_gt-0.8.aln' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
aln='amastins.trimal_gt-0.8.aln'
guide='guide_amastins'
guide_tree=$guide'.treefile'
bb=1000
nm=5000

# iqtree2 -m LG+G4 -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --prefix $guide
# iqtree2 -m LG+C20+G4 -T AUTO --threads-max $PBS_NUM_PPN -B $bb --nmax $nm --quiet --safe -s $aln --tree-freq $guide_tree

# iqtree2 -m TEST -madd C10,C20,C30,C40,C50,C60,LG4M,LG4X,LG+F+G,LG+C10+G,LG+C20+G,LG+C30+G,LG+C40+G,LG+C60+G \
# 	-T AUTO --threads-max $PBS_NUM_PPN -B $bb --nmax $nm --quiet --safe -s $aln

# iqtree -m TEST -bb $bb -nm $nm -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln
# iqtree -m GTR+G -bb $bb -nm $nm -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln

iqtree -m LG+G4 -nt AUTO -ntmax $PBS_NUM_PPN -quiet -safe -s $aln -pre $guide
iqtree -m LG+C20+G4 -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -safe -s $aln -ft $guide_tree #-wsr

#copy files back
rm $aln
cp * $datadir
