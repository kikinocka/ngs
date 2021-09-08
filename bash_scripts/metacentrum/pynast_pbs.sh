#!/bin/bash
#PBS -N pynast
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add qiime-1.9.1

data_dir='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/metamonada/'

#copy files to scratch
cp $data_dir'metamonads_eukref.barthelona.anaeramoeba.aln' $SCRATCHDIR
cp $data_dir'metamonads_otus.fa' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR


existing='metamonads_eukref.barthelona.anaeramoeba.aln'
add='metamonads_otus.fa'
aln='metamonads_V9.pynast.aln'
log='metamonads_V9.pynast.log'

pynast -a $aln -g $log -i $add -t $existing


#copy files back
rm $existing $add
cp * $data_dir
