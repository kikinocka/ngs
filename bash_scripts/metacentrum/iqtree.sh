#!/bin/bash
#PBS -N IQT
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
# module add iqtree-1.6.12
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load iqtree

datadir='/storage/brno3-cerit/home/kika/diplonema/isopropanol_dehydrogenase/ver2/'

#copy files to scratch
# cp $datadir'/'*.aln $SCRATCHDIR
cp $datadir'adh.trimal_gt-0.8.aln' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
aln='adh.trimal_gt-0.8.aln'
guide='guide_adh'
guide_tree=$guide'.treefile'
bb=1000
nm=5000

iqtree2 -m TEST -madd C10,C20,C30,C40,C50,C60,LG4M,LG4X,LG+F+G,LG+C10+F+G,LG+C20+F+G,LG+C30+F+G,LG+C40+F+G,LG+C60+F+G \
	-B $bb --nmax $nm -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln

# iqtree -m TEST -bb $bb -nm $nm -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln
# iqtree -m GTR+G -bb $bb -nm $nm -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln

# iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -safe -s $aln -pre $guide
# iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -safe -s $aln -ft $guide_tree #-wsr

#copy files back
rm $aln
cp * $datadir
