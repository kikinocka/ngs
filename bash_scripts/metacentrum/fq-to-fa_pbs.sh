#!/bin/bash
#PBS -N fastx
#PBS -l select=1:ncpus=10:mem=10gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add fastx-0.0.14

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/reads/'

#copy files to scratch
cp $datadir'BML_trimmed_2.fq' $SCRATCHDIR

fq='BML_trimmed_2.fq'
fa='BML_trimmed_2.fa'

#run on scratch
cd $SCRATCHDIR

fastq_to_fasta -n -i $fq -o $fa

#copy files back
rm $fq
cp -R * $datadir
