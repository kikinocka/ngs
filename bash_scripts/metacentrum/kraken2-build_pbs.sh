#!/bin/bash
#PBS -N kraken-build
#PBS -l select=1:ncpus=20:mem=2gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add kraken2-1.0

db_dir='/storage/brno3-cerit/home/kika/databases/kraken2'

#compute on scratch
cd $SCRATCHDIR

kraken2-build --standard --db kraken2-db --threads $PBS_NUM_PPN

#copy files back
rm $assembly
cp -R * $db_dir
