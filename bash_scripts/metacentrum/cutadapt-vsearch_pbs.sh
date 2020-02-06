#!/bin/bash
#PBS -N cutadapt-vsearch
#PBS -l select=1:ncpus=1:mem=150gb:scratch_local=100gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add python36-modules-gcc
module add vsearch-1.4.4

sl='/storage/brno3-cerit/home/kika/sl_euglenozoa/'
merged=$sl'merged_pear'
out=$sl'trimmed_cutadapt'

#copy file to scratch
cp $merged/*.assembled.fastq $SCRATCHDIR
cp $sl'clean_fastq_files.sh' $SCRATCHDIR
cp $sl'hashing.py' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
CUTADAPT_SCRIPT='clean_fastq_files.sh'

for f in *.assembled.fastq ; do
 # V4 or V9 as an option
 bash ${CUTADAPT_SCRIPT} ${f} V9
done

#copy files back
rm 'clean_fastq_files.sh' 'hashing.py' *.assembled.fastq
cp * $out
