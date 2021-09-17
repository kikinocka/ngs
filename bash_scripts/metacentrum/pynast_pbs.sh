#!/bin/bash
#PBS -N pynast
#PBS -l select=1:ncpus=1:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add qiime-1.9.1

data_dir='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/metamonada/'

#copy files to scratch
cp $data_dir'arb-silva.de_2021-09-16_id1053505.upd.aln' $SCRATCHDIR
cp $data_dir'metamonads_eukref-otus.unambiguous.fa' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR


existing='arb-silva.de_2021-09-16_id1053505.upd.aln'
add='metamonads_eukref-otus.unambiguous.fa'
aln='metamonads_V9.pynast.aln'
log='metamonads_V9.pynast.log'
length=50

pynast -a $aln -g $log -l $length -i $add -t $existing


#copy files back
rm $existing $add
cp * $data_dir
