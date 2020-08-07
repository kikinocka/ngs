#!/bin/bash
#PBS -N bam2len
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb:os=debian10
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add py-telomeracat/py-telomeracat-3.3.0-intel-19.0.4-knqay2h

data_dir='/storage/brno3-cerit/home/kika/kinetoplastids/lpyr_genome/'

#copy files to scratch
cp $data_dir'bw2_mapping/lpyr_bw2_sorted.bam' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

bam='lpyr_bw2_sorted.bam'
output='lpyr_telomerecat.csv'
format=1
# 0: No output [Default]
# 1: Total Reads Processed
# 2: Detailed output

telomerecat bam2length -p $PBS_NUM_PPN -v $format --output $output $bam

#copy files back
rm $bam
cp -R * $data_dir
