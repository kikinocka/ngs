#!/bin/bash
#PBS -N IQT
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree

datadir='/storage/brno12-cerit/home/kika/quinones/ver12/'

#copy files to scratch
cp $datadir'ubiG.trimal_gt-0.8.aln' $SCRATCHDIR
# cp $datadir'guide'* $SCRATCHDIR
# cp $datadir'spp_constr.tre' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
aln='ubiG.trimal_gt-0.8.aln'
guide='guide_ubiG'
guide_tree=$guide'.treefile'
# constr='spp_constr.tre'
bb=1000
nm=10000


iqtree3-mpi -m LG+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --prefix $guide
iqtree3-mpi -m LG+C60+G4 -T $PBS_NUM_PPN -B $bb --alrt $nm --nmax $nm --quiet --safe -s $aln --tree-freq $guide_tree --boot-trees
# -g $constr 

# iqtree -m MFP --mset C20,C40,C60,LG4M,LG4X,LG+F+G,LG+C20+G,LG+C40+G,LG+C60+G,LG+PMSF+G \
# 	-T AUTO --threads-max $PBS_NUM_PPN -B $bb --nmax $nm --quiet --safe -s $aln

#copy files back
rm $aln #$constr
cp * $datadir
