#!/bin/bash
#PBS -N kraken-build
#PBS -l select=1:ncpus=20:mem=100gb:scratch_local=100gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add kraken2-1.0

db_dir='/storage/brno3-cerit/home/kika/databases/'

#compute on scratch
cd $SCRATCHDIR

kraken2-build --standard --db kraken2DB --threads $PBS_NUM_PPN

#copy files back
cp -R * $db_dir
