#!/bin/bash
#PBS -N kraken-build
#PBS -l select=1:ncpus=20:ompthreads=20:mem=350gb:scratch_local=650gb
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add kraken2-1.2

db_dir='/storage/brno3-cerit/home/kika/databases/'

#copy files to scratch
cp $db_dir'eukprot_v2_proteins_renamed.taxids.faa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
db='kraken2DB-eukprot'
eukprot='eukprot_v2_proteins_renamed.taxids.faa'

echo '*** DOWNLOADING TAXONOMY ***'
kraken2-build --download-taxonomy --threads $PBS_NUM_PPN --db $db
echo '*** TAXONOMY DOWNLOADED ***'

# echo '*** DOWNLOADING NUCLEOTIDE DATABASE ***'
# kraken2-build --download-library nt --threads $PBS_NUM_PPN --db $db
# echo '*** NUCLEOTIDE DATABASE DOWNLOADED ***'

echo '*** DOWNLOADING DATABASES ***'
kraken2-build --download-library archaea --threads $PBS_NUM_PPN --db $db
kraken2-build --download-library bacteria --threads $PBS_NUM_PPN --db $db
kraken2-build --download-library plasmid --threads $PBS_NUM_PPN --db $db
kraken2-build --download-library viral --threads $PBS_NUM_PPN --db $db
kraken2-build --download-library human --threads $PBS_NUM_PPN --db $db
kraken2-build --download-library fungi --threads $PBS_NUM_PPN --db $db
kraken2-build --download-library plant --threads $PBS_NUM_PPN --db $db
kraken2-build --download-library protozoa --threads $PBS_NUM_PPN --db $db
kraken2-build --download-library UniVec_Core --threads $PBS_NUM_PPN --db $db
echo '*** DATABASES DOWNLOADED ***'

echo '*** ADDING EUKPROT ***'
kraken2-build --add-to-library $eukprot --threads $PBS_NUM_PPN --db $db
echo '*** EUKPROT ADDED ***'

echo '*** BUILDING KRAKEN2 DATABASE ***'
kraken2-build --build --threads $PBS_NUM_PPN --db $db
echo '*** KRAKEN2 DATABASE BUILT ***'

echo '*** CLEANING KRAKEN2 DATABSE ***'
kraken2-build --clean --threads $PBS_NUM_PPN --db $db
echo '*** KRAKEN2 DATABASE CLEAN ***'

#copy files back
cp -R * $db_dir
