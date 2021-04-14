#!/bin/bash
#PBS -N SPAdes
#PBS -l select=1:ncpus=50:ompthreads=50:mem=150gb:scratch_local=30gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add spades-3.14.0

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/'
reads=$datadir'reads/'

#copy reads to scratch
cp $reads'BML_trimmed_1.fq.gz' $reads'BML_trimmed_2.fq.gz' $SCRATCHDIR

pe1_1='BML_trimmed_1.fq.gz'
pe1_2='BML_trimmed_2.fq.gz'
out='spades_kmers'

#compute on scratch
cd $SCRATCHDIR

# #metagenome assembly
# metaspades.py --pe-1 1 $pe1_1 --pe-2 1 $pe1_2 -t $PBS_NUM_PPN -o BML_metagenome

#metagenome specifying k-mers
metaspades.py --pe-1 1 $pe1_1 --pe-2 1 $pe1_2 -k 21,33,55,77,99,111  -t $PBS_NUM_PPN -o $out

# #using reference genome
# spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 --trusted-contigs $cbom --careful -t $PBS_NUM_PPN -o spades_cbom_trusted

# #single-cell using several libraries
# spades.py --sc --careful -t $PBS_NUM_PPN -o out \
# --pe1-m $pe1m --pe1-1 $pe11 --pe1-2 $pe12 --pe1-s $pe1u \
# --pe2-m $pe2m --pe2-1 $pe21 --pe2-2 $pe22 --pe2-s $pe2u \

#copy results back
rm $pe1_1 $pe1_2
cp -r * $datadir
