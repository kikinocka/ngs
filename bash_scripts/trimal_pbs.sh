#!/bin/bash
#PBS -N trimAl
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add trimal-1.4

data_dir='/storage/brno3-cerit/home/kika/euglenophytes/trees/helicases/'

#copy files to scratch
cp $data_dir'helicases_mafft.fa' $SCRATCHDIR

aln='helicases_mafft.fa'
trimmed='helicases_trimal_automated1.aln'
option='automated1'

#compute on scratch
cd $SCRATCHDIR
trimal -in $aln -out $trimmed -$option -fasta

#copy files back
cp $trimmed $data_dir
