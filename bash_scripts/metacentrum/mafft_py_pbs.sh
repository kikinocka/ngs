#!/bin/bash
#PBS -N MAFFT
#PBS -l select=1:ncpus=20:mem=30gb:scratch_local=1gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add mafft-7.313

data_dir='/storage/brno3-cerit/home/kika/sags/alignments/'
script='/storage/brno2/home/kika/scripts/kika/py_scripts/run_program/mafft_pbs.py'

#copy files to scratch
cp $data_dir'*.faa' $SCRATCHDIR
cp $script $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

python3 $script

#copy files back
cp *.aln $data_dir
