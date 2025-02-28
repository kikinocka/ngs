#!/bin/bash
#PBS -N IQT
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree

datadir='/storage/brno12-cerit/home/kika/trafficking/clathrin/'

#copy files to scratch
cp $datadir'CHC_opisthokonta.man_trimmed.aln' $SCRATCHDIR
cp $datadir'guide'* $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
aln='CHC_opisthokonta.man_trimmed.aln'
guide='guide_CHC_opist'
guide_tree=$guide'.treefile'
bb=1000
nm=5000


# iqtree -m LG+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --prefix $guide
iqtree -m LG+C60+G -T $PBS_NUM_PPN -B $bb --nmax $nm --quiet --safe -s $aln --tree-freq $guide_tree --boot-trees

# iqtree -m TEST -madd C10,C20,C30,C40,C50,C60,LG4M,LG4X,LG+F+G,LG+C10+G,LG+C20+G,LG+C30+G,LG+C40+G,LG+C60+G \
# 	-T $PBS_NUM_PPN -B $bb --nmax $nm --quiet --safe -s $aln --tree-freq $guide_tree --boot-trees


#copy files back
rm $aln
cp * $datadir
