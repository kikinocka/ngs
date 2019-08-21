#!/bin/bash
#PBS -N trimAl
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add trimal-1.4

data_dir='/storage/brno3-cerit/home/kika/catalase/apx_tree/ver6/'

#copy files to scratch
cp $data_dir'apx_mafft.aln' $SCRATCHDIR

aln='apx_mafft.aln'
trimmed='apx_trimal_automated1.aln'
option='automated1'

#compute on scratch
cd $SCRATCHDIR
trimal -in $aln -out $trimmed -$option -fasta
# trimal -in $aln -out $trimmed -gt $option -fasta

#copy files back
cp $trimmed $data_dir
