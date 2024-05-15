#!/bin/bash
#PBS -N IQT-AU
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree

datadir='/storage/brno12-cerit/home/kika/trafficking/diplonemids_all/ARFs/ph-arf/ver2/'

#copy files to scratch
cp $datadir'iqtree/arfs_reduced.trimal_gt-0.8.aln' $SCRATCHDIR
cp $datadir'iqtree/arfs_reduced.trimal_gt-0.8.aln.treefile' $SCRATCHDIR
cp $datadir'iqtree/arfs_reduced.trimal_gt-0.8.aln.ufboot' $SCRATCHDIR
cp $datadir'au_test/arfs_reduced.constr1' $SCRATCHDIR


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
pref='arfs_reduced'
aln='arfs_reduced.trimal_gt-0.8.aln'
ufb_trees='arfs_reduced.trimal_gt-0.8.aln.ufboot'
ml_tree='arfs_reduced.trimal_gt-0.8.aln.treefile'
constr1='arfs_reduced.constr1'
ufb=1000

iqtree2 -m LG+C20+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln -g $constr1 --prefix $pref.constr1
cat $ml_tree $pref.constr1.treefile $ufb_trees > $pref.trees
iqtree2 -m LG+C20+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --trees $pref.trees --test-weight --test-au --test 10000 -n 0


#copy files back
rm $aln $constr1 $ufb_trees
cp * $datadir'au_test/'
