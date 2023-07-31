#!/bin/sh
#PBS -N gappa_accumulate
#PBS -l select=1:ncpus=20:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

gappa='/storage/brno3-cerit/home/kika/miniconda3/bin/gappa'
data='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/metamonads/placement/'

#copy files to scratch
cp $data'RAxML_portableTree.EPARUN_metamonads.jplace' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

jplace='RAxML_portableTree.EPARUN_metamonads.jplace'
prefix=${jplace%.jplace}.accumulated
log=${jplace%.jplace}.accumulated.log
threshold=0.8

$gappa edit accumulate --jplace-path $jplace --threshold $threshold --file-prefix $prefix --threads $PBS_NUM_PPN --log-file $log


#copy files back
rm $jplace
cp -R * $data
