#!/bin/sh
#PBS -N gappa_accumulate
#PBS -l select=1:ncpus=20:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

gappa='/storage/brno3-cerit/home/kika/miniconda3/bin/gappa'
data='/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/euglenozoa/placement/'

#copy files to scratch
cp $data'RAxML_portableTree.EPARUN_euglenozoa.jplace' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

jplace='RAxML_portableTree.EPARUN_euglenozoa.jplace'
prefix=${jplace%.jplace}.
log=${jplace%.jplace}.accumulated.log
threshold=0.8

$gappa edit accumulate --jplace-path $jplace --threshold $threshold --file-prefix $prefix --threads $PBS_NUM_PPN --log-file $log


#copy files back
rm $jplace
cp -R * $data
