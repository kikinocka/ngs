#!/bin/bash
#PBS -N MAFFT
#PBS -l select=1:ncpus=20:mem=15gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add mafft-7.313

data_dir='/storage/brno3-cerit/home/kika/euglenophytes/trees/helicases/'

#copy files to scratch
cp $data_dir'helicases.aln' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
seqs='helicases.fa'
aln='helicases_mafft.aln'

mafft --thread $PBS_NUM_PPN --inputorder --auto $seqs > $aln

#copy files back
cp $aln $data_dir
