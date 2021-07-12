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

db='kraken2DB'

echo '*** DOWNLOADING TAXONOMY ***'
kraken2-build --download-taxonomy --threads $PBS_NUM_PPN --db $db
echo '*** TAXONOMY DOWNLOADED ***'

echo '*** DOWNLOADING NUCLEOTIDE DATABASE ***'
kraken2-build --download-library nt --threads $PBS_NUM_PPN --db $db
echo '*** NUCLEOTIDE DATABASE DOWNLOADED ***'

echo '*** BUILDING KRAKEN2 DATABASE ***'
kraken2-build --build --threads $PBS_NUM_PPN --db $db
echo '*** KRAKEN2 DATABASE BUILT ***'

#copy files back
cp -R * $db_dir
