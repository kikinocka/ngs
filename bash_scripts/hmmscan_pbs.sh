#!/bin/bash
#PBS -N hmmscan
#PBS -l select=1:ncpus=10:mem=10gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add hmmer-3.2

data_dir='/storage/brno3-cerit/home/kika/elonga/'
pfam_dir='/storage/brno3-cerit/home/kika/pfam/'

#copy files to scratch
cp $pfam_dir'Pfam-A.hmm' $SCRATCHDIR
cp $data_dir'el_DEEZ.fasta' $SCRATCHDIR

hmm='Pfam-A.hmm'
proteins='el_DEEZ.fasta'

#compute on scratch
cd $SCRATCHDIR
hmmpress $hmm
hmmscan --cpu $PBS_NUM_PPN --domtblout el_DEEZ.pfam.domtblout $hmm $proteins

#copy files back
cp el_DEEZ.pfam.domtblout $data_dir
