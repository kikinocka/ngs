#!/bin/bash
#PBS -N cutadapt-vsearch
#PBS -l select=1:ncpus=1:mem=150gb:scratch_local=500gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add python36-modules-gcc
module add vsearch-1.4.4

TMP_FASTA=$(mktemp)
TMP_FASTA_DEREPLICATED=$(mktemp)

if [ $# != 1 ]; then
    echo "You need to supply an output filename";
    exit 1;
fi

cat ./*.fas > ${TMP_FASTA}

# Dereplicate (vsearch)
vsearch --threads $PBS_NUM_PPN \
    --derep_fulllength ${TMP_FASTA} \
    --sizein \
    --sizeout \
    --fasta_width 0 \
    --output $1

bzip2 -9k $1 &

rm ${TMP_FASTA} ${TMP_FASTA_DEREPLICATED}
