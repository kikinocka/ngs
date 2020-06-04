#!/bin/bash
#PBS -N SPAdes
#PBS -l select=1:ncpus=10:ompthreads=10:mem=30gb:scratch_local=30gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add spades-3.14.0

reads='/storage/brno3-cerit/home/kika/kinetoplastids/cbom_genome/reads/'
outdir='/storage/brno3-cerit/home/kika/kinetoplastids/cbom_genome/'

#copy reads to scratch
cp $reads'AK08_047.R1.trim.fq.gz' $reads'AK08_047.R2.trim.fq.gz' $SCRATCHDIR

pe1_1='AK08_047.R1.trim.fq.gz'
pe1_2='AK08_047.R2.trim.fq.gz'

#compute on scratch
cd $SCRATCHDIR
spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 --careful -t $PBS_NUM_PPN -o spades


# spades.py --sc --careful -t $PBS_NUM_PPN -o out \
# --pe1-m $pe1m --pe1-1 $pe11 --pe1-2 $pe12 --pe1-s $pe1u \
# --pe2-m $pe2m --pe2-1 $pe21 --pe2-2 $pe22 --pe2-s $pe2u \

#copy results back
rm $pe1_1 $pe1_2
cp -r * $outdir
