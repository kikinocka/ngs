#!/bin/bash
#PBS -N pear
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=100gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe
cat $PBS_NODEFILE

#add module
module add pear-0.9.11

raw='/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/raw_reads'
merged='/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/merged_pear/'

#copy files to scratch
cp $raw'/'*.gz $SCRATCHDIR
# cp $raw/*.bz2 $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
# WORKING_DIR=`pwd`
# SAMPLE_DIR='/storage/brno3-cerit/home/kika/sl_euglenozoa/raw_reads/'
# echo 'Working Dir: ' ${WORKING_DIR}
# echo ' Sample Dir: ' ${SAMPLE_DIR}

# echo 'IGNORE PERMISSION DENIED ERRORS'

# # find ${SAMPLE_DIR} -name '*.gz' | \
# find ${SAMPLE_DIR} -name '*.bz2' | \
# while read R1 ; do
#  cp ${R1} ${WORKING_DIR}
#  cp ${R1/R1/R2} ${WORKING_DIR}
# done

gunzip *.gz
# bzip2 -d *.bz2

find . -name '*_R1_001.fastq' | \
while read R1 ; do
    pear -j $PBS_NUM_PPN -f ${R1} -r ${R1/R1/R2} -o ${R1/_L001_R1_001.fastq/}
    #comment out this line if you want to keep the other files - probably not
    rm -f ${R1/_L001_R1_001.fastq/}{.discarded,.unassembled.{forward,reverse}}.fastq
done

#copy files back
cp *assembled.fastq $merged
