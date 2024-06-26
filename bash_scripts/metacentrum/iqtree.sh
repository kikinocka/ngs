#!/bin/bash
#PBS -N IQT
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree-2.2.0

datadir='/storage/brno12-cerit/home/kika/trafficking/mantamonas/rabs/ver3/'

#copy files to scratch
cp $datadir'rabs.trimal_gt-0.8.aln' $SCRATCHDIR
# cp $datadir'/'* $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
aln='rabs.trimal_gt-0.8.aln'
guide='guide_rabs'
guide_tree=$guide'.treefile'
bb=1000
nm=5000

iqtree2 -m LG+G4 -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --prefix $guide
iqtree2 -m LG+C20+G4 -T 15 --threads-max $PBS_NUM_PPN -B $bb --nmax $nm --quiet --safe -s $aln --tree-freq $guide_tree --boot-trees

# iqtree2 -m TEST -madd C10,C20,C30,C40,C50,C60,LG4M,LG4X,LG+F+G,LG+C10+G,LG+C20+G,LG+C30+G,LG+C40+G,LG+C60+G \
# 	-T AUTO --threads-max $PBS_NUM_PPN -B $bb --nmax $nm --quiet --safe -s $aln

# iqtree -m TEST -bb $bb -nm $nm -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln
# iqtree -m GTR+G -bb $bb -nm $nm -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln

# iqtree -m LG+G4 -nt AUTO -ntmax $PBS_NUM_PPN -quiet -safe -s $aln -pre $guide
# iqtree -m LG+C20+G4 -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -nm $nm -quiet -safe -s $aln -ft $guide_tree #-wsr

# iqtree -m LG+C20+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -nm $nm -quiet -safe -s $aln -pre ${aln%.aln}


#copy files back
rm $aln
cp * $datadir
