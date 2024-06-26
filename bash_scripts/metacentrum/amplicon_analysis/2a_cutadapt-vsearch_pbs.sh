#!/bin/bash
#PBS -N cutadapt-vsearch
#PBS -l select=1:ncpus=1:mem=10gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add python36-modules-gcc
module add vsearch-1.4.4

scripts='/storage/brno2/home/kika/scripts/bash_scripts/metacentrum/amplicon_analysis/'
data='/storage/brno3-cerit/home/kika/oil_sands/V4-sediment/'
merged=$data'merged_pear'
out=$data'trimmed_cutadapt'

#copy files to scratch
cp $merged'/'*.assembled.fastq $SCRATCHDIR
cp $scripts'2b_clean_fastq_files.sh' $SCRATCHDIR
# cp $sl'hashing.py' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
CUTADAPT_SCRIPT='2b_clean_fastq_files.sh'

export TMPDIR=$SCRATCHDIR

for f in *.assembled.fastq ; do
 # V4 or V9 as an option
 bash ${CUTADAPT_SCRIPT} ${f} V4
done

#copy files back
rm *.assembled.fastq '2b_clean_fastq_files.sh' #'hashing.py'
cp * $out
