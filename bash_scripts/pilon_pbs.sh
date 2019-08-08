#!/bin/bash
#PBS -N Pilon
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=100gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add openjdk-10

data_dir='/storage/brno3-cerit/home/kika/p57/'

#copy files to scratch
cp $data_dir'pilon1/p57_pilon1.fa' $SCRATCHDIR
cp $data_dir'pilon1/p57_pilon1_bw2_sorted.bam' $SCRATCHDIR
cp $data_dir'pilon1/p57_pilon1_bw2_sorted.bam.bai' $SCRATCHDIR

pilon='/storage/brno2/home/kika/tools/pilon-1.23.jar'
assembly='p57_pilon1.fa'
bam='p57_pilon1_bw2_sorted.bam'
index='p57_pilon1_bw2_sorted.bam.bai'

#compute on scratch
cd $SCRATCHDIR
java -jar -Xmx20G $pilon --genome $assembly --bam $bam --threads $PBS_NUM_PPN

#copy results to your folder
rm $assembly $bam $index
cp -r * $data_dir/. || export CLEAN_SCRATCH=false
