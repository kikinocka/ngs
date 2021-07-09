#!/bin/bash
#PBS -N kraken-build
#PBS -l select=1:ncpus=20:mem=2gb:scratch_local=100gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add kraken2-1.0

db_dir='/storage/brno3-cerit/home/kika/databases/'

#compute on scratch
cd $SCRATCHDIR

kraken2-build --download-library nt --db kraken2DB --use-ftp 
kraken2-build --build --db kraken2DB --clean
# kraken2-build --standard --db kraken2DB --threads $PBS_NUM_PPN

#copy files back
cp -R * $db_dir
