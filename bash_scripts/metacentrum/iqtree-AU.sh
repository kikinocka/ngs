#!/bin/bash
#PBS -N IQT-AU
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree

datadir='/storage/brno12-cerit/home/kika/kinetoplastids/kinesins/kin2/ver6/'

#copy files to scratch
cp $datadir'kinesins.trimal_gt-0.8.aln' $SCRATCHDIR
cp $datadir'kinesins.trimal_gt-0.8.aln.ufboot' $SCRATCHDIR
cp $datadir'au_test/kinesins.constr1' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

# #calculate UFB trees and then perform AU test
# pref='sec13'
# aln='sec13.trimal_gt-0.8.aln'
# constr1='sec13.constr1'
# constr2='sec13.constr2'
# ufb=1000

# iqtree2 -m LG+C20+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --prefix $pref.unconstr -B $ufb --boot-trees
# iqtree2 -m LG+C20+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln -g $constr1 --prefix $pref.constr1
# iqtree2 -m LG+C20+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln -g $constr2 --prefix $pref.constr2
# cat $pref.unconstr.ufboot $pref.constr*.treefile > $pref.trees
# iqtree2 -m LG+C20+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --trees $pref.trees --test-weight --test-au --test 10000 -n 0


#already having UFB trees; perform only AU test
pref='kinesins'
aln='kinesins.trimal_gt-0.8.aln'
ufb_trees='kinesins.trimal_gt-0.8.aln.ufboot'
constr1='kinesins.constr1'
ufb=1000

iqtree2 -m LG+C20+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln -g $constr1 --prefix $pref.constr1
cat $ufb_trees $pref.constr1.treefile > $pref.trees
iqtree2 -m LG+C20+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --trees $pref.trees --test-weight --test-au --test 10000 -n 0


#copy files back
rm $aln $constr1 $ufb_trees
cp * $datadir'au_test/'
