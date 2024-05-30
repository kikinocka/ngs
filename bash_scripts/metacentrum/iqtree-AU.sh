#!/bin/bash
#PBS -N IQT-AU
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree-2.2.0

datadir='/storage/brno12-cerit/home/kika/trafficking/diplonemids_all/ARFs/ph-arf/ver3/au_test/'

#copy files to scratch
cp $datadir'arfs_reduced.trimal_gt-0.8.aln' $SCRATCHDIR
cp $datadir'RAxML_bipartitions.arfs_reduced.renamed.tre' $SCRATCHDIR
cp $datadir'arfs_reduced.trimal_gt-0.8.aln_renamed.tre' $SCRATCHDIR
cp $datadir'arfs_reduced.trimal_gt-0.8.aln_renamed.ufboot' $SCRATCHDIR
cp $datadir'arfs_reduced.constr'* $SCRATCHDIR

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
rax_tree='RAxML_bipartitions.arfs_reduced.renamed.tre'
iqt_tree='arfs_reduced.trimal_gt-0.8.aln_renamed.tre'
ufb_trees='arfs_reduced.trimal_gt-0.8.aln_renamed.ufboot'

for constr in arfs_reduced.constr*tre ; do 
	echo $constr
	name=${constr%.tre}
	iqtree2 -m LG+C20+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln -g $constr --prefix $name
done
cat $rax_tree $iqt_tree $pref.constr*.treefile $ufb_trees > $pref.trees
iqtree2 -m LG+C20+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --trees $pref.trees --test-weight --test-au --test 10000 -n 0


#copy files back
rm $aln $rax_tree $iqt_tree $ufb_trees arfs_reduced.constr*tre
cp * $datadir
