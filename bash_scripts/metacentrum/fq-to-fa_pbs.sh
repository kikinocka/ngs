#!/bin/bash
#PBS -N fastx
#PBS -l select=1:ncpus=10:mem=10gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add fastx-0.0.14

datadir='/storage/brno3-cerit/home/kika/tRNAs-kinetoplastids/read_DB/'

#copy files to scratch
cp $datadir'2-T-brucei-cyto.fastq' $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

fq='2-T-brucei-cyto.fastq'
fa='Tbrucei-cyto.fa'

fastq_to_fasta -n -i $fq -o $fa

#copy files back
rm $fq
cp -R * $datadir
