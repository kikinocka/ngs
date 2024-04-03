#!/bin/bash
#PBS -N IQT-AU
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree

datadir='/storage/brno12-cerit/home/kika/kinetoplastids/kinesins/kin2/ver6/'

#copy files to scratch
cp $datadir'kinesins.trimal_gt-0.8.aln' $SCRATCHDIR
cp $datadir'kinesins.trimal_gt-0.8.aln.ufboot' $SCRATCHDIR
cp $datadir'kinesins.trimal_gt-0.8.constr1' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
pref='kinesins.trimal_gt-0.8'
aln='kinesins.trimal_gt-0.8.aln'
boottrees='kinesins.trimal_gt-0.8.aln.ufboot'
constr1='kinesins.trimal_gt-0.8.constr1'
# constr2='sec13.constr2'
ufb=1000

# iqtree2 -m LG+C20+G -T 15 --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --prefix $pref.unconstr -B $ufb --boot-trees
iqtree2 -m LG+C20+G -T 15 --threads-max $PBS_NUM_PPN --quiet --safe -s $aln -g $constr1 --prefix $pref.constr1
# iqtree2 -m LG+C20+G -T 15 --threads-max $PBS_NUM_PPN --quiet --safe -s $aln -g $constr2 --prefix $pref.constr2
# cat $pref.unconstr.ufboot $pref.constr*.treefile > $pref.trees
cat $boottrees $pref.constr*.treefile > $pref.trees
iqtree2 -m LG+C20+G -T 15 --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --trees $pref.trees --test-weight --test-au --test 10000 -n 0

#copy files back
rm $aln $constr1 $boottrees
cp * $datadir
