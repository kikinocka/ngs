#!/bin/bash
#PBS -N cutadapt-vsearch
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add python36-modules-gcc
module add vsearch-1.4.4

WORKING_DIR='/storage/brno3-cerit/home/kika/sl_euglenozoa/'

cd $WORKING_DIR
CUTADAPT_SCRIPT='clean_fastq_files.sh'

for f in 'merged_pear/'*.assembled.fastq ; do
 # V4 or V9 as an option
 bash ${CUTADAPT_SCRIPT} ${f} V9
done
