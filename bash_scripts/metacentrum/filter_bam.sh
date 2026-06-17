#!/bin/bash
#PBS -N filter_bam
#PBS -l select=1:ncpus=1:mem=100gb:scratch_local=100gb
#PBS -l walltime=168:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

data_dir='/storage/brno12-cerit/home/kika/egracilis/chinese/'
script_dir='/storage/brno12-cerit/home/kika/scripts/py_scripts/'

#copy files to scratch
cp $data_dir'EG_chin_ht2.sorted.bam'* $SCRATCHDIR
cp $script_dir'filter_bam.py' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

script='filter_bam.py'
bam='EG_chin_ht2.sorted.bam'

module add python36-modules-gcc
python3 $script $bam
module unload python

module load samtools
samtools index *.pass.bam
module unload samtools

#copy files back
rm $bam $bam'.bai' $script
cp -r * $data_dir && clean_scratch
