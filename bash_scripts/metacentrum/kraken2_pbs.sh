#!/bin/bash
#PBS -N kraken
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=10gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add kraken2-1.2

kraken2DB='/storage/brno3-cerit/home/kika/databases/kraken2DB'
datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/20xx0821_BML-B-first/'

#copy files to scratch
cp $datadir'bml_meta.spades_def.fa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

assembly='bml_meta.spades_def.fa'
classified='bml_meta.classified.fa'
unclassified='bml_meta.unclassified.fa'
out='bml_meta.kraken.out'
report='bml_meta.kraken.report'

kraken2 --db $kraken2DB --threads $PBS_NUM_PPN \
  --classified-out $classified \
  --unclassified-out $unclassified \
  --report $report $assembly > $out

#copy files back
rm $assembly
cp -R * $datadir'kraken2/'
