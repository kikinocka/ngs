#!/bin/bash
#PBS -N SPAdes
#PBS -l select=1:ncpus=50:ompthreads=50:mem=100gb:scratch_local=30gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add spades-3.14.0

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P1B_1-05C_L001-ds.ec8b691bd68b44deb59919ca3da275ba/'
reads=$datadir'1-reads/'

#copy reads to scratch
cp $reads'P1B_deep_trimmed_1.fq.gz' $reads'P1B_deep_trimmed_2.fq.gz' $SCRATCHDIR
cp $reads'P1B_trimmed_1.fq.gz' $reads'P1B_trimmed_2.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

fwd1='P1B_deep_trimmed_1.fq.gz'
rev1='P1B_deep_trimmed_2.fq.gz'
fwd2='P1B_trimmed_1.fq.gz'
rev2='P1B_trimmed_2.fq.gz'

#metagenome assembly
metaspades.py -t $PBS_NUM_PPN \
	--pe1-1 $fwd1 --pe1-2 $rev1 \
	--pe2-1 $fwd2 --pe2-2 $rev2 \
	-o $SCRATCHDIR

# #metagenome specifying k-mers
# metaspades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 -k 21,33,55,77,99,111  -t $PBS_NUM_PPN -o spades_kmers

# #using reference genome
# spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 --trusted-contigs $cbom --careful -t $PBS_NUM_PPN -o spades_cbom_trusted

# #single-cell using several libraries
# spades.py --sc --careful -t $PBS_NUM_PPN -o out \
# --pe1-m $pe1m --pe1-1 $pe11 --pe1-2 $pe12 --pe1-s $pe1u \
# --pe2-m $pe2m --pe2-1 $pe21 --pe2-2 $pe22 --pe2-s $pe2u \

#copy results back
rm *gz
cp -r * $datadir'2-spades/'
