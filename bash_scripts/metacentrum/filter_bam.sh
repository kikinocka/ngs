#!/bin/bash
#PBS -N filter_bam
#PBS -l select=1:ncpus=1:mem=20gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add python36-modules-gcc


data='/storage/brno12-cerit/home/kika/paratrimastix/hisat2/illumina/'
script='/storage/brno12-cerit/home/kika/scripts/py_scripts/filter_bam.py'

#copy files to scratch
cp $data'PaPyr_ht2_sorted.bam' $SCRATCHDIR
cp $script $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

bam='PaPyr_ht2_sorted.bam'

python3 $script $bam


#copy files back
rm $bam
cp -r * $data
