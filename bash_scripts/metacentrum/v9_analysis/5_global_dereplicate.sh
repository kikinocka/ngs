#!/bin/bash
#PBS -N vsearch
#PBS -l select=1:ncpus=1:mem=50gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add vsearch-1.4.4

data='/storage/brno3-cerit/home/kika/sl_euglenozoa/'
trimmed=$data'trimmed_cutadapt'

#copy file to scratch
cp $trimmed'/'*.fas $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
out='global_dereplicated.fa'
export TMPDIR=$SCRATCHDIR

TMP_FASTA=$(mktemp)
TMP_FASTA_DEREPLICATED=$(mktemp)

# if [ $# != 1 ]; then
#     echo "You need to supply an output filename";
#     exit 1;
# fi

cat ./*.fas > ${TMP_FASTA}

# Dereplicate (vsearch)
vsearch --threads 1 \
    --derep_fulllength ${TMP_FASTA} \
    --sizein \
    --sizeout \
    --fasta_width 0 \
    --output ${out}

bzip2 -9k ${out} &

#copy files back
rm ${TMP_FASTA} ${TMP_FASTA_DEREPLICATED}
cp * $data
