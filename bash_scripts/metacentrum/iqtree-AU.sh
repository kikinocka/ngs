#!/bin/bash
#PBS -N IQT-AU
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-2.2.0

datadir='/storage/brno3-cerit/home/kika/diplonema/cardiolipin/CLD1/ver5_AU'

#copy files to scratch
# cp $datadir'/'* $SCRATCHDIR
cp $datadir'/'* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
pref='cld'
aln='cld.trimal_gt-0.8.aln'
constr1='cld.constr1'
# constr2='sec13.constr2'
ufb=1000

iqtree2 -m LG+C20+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln --prefix $pref.unconstr -B $ufb --boot-trees
iqtree2 -m LG+C20+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -g $constr1 --prefix $pref.constr1
# iqtree2 -m LG+C20+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -g $constr2 --prefix $pref.constr2
cat $pref.unconstr.ufboot $pref.constr*.treefile > $pref.trees
iqtree2 -m LG+C20+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln --trees $pref.trees --test-weight --test-au --test 10000 -n 0

#copy files back
# rm $aln $constr
cp * $datadir
