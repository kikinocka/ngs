#!/bin/bash
#PBS -N filter_bam
#PBS -l select=1:ncpus=1:mem=20gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load samtools
module add python36-modules-gcc


data_dir='/storage/brno12-cerit/home/kika/paratrimastix/hisat2/illumina/'
script_dir='/storage/brno12-cerit/home/kika/scripts/py_scripts/'

#copy files to scratch
cp $data_dir'PaPyr_ht2_sorted.bam'* $SCRATCHDIR
cp $script_dir'filter_bam.py' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

script='filter_bam.py'
bam='PaPyr_ht2_sorted.bam'

python3 $script $bam
samtools index *.pass.bam

#copy files back
rm $bam $bam'.bai' $script
cp -r * $data_dir
