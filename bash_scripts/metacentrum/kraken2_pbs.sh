#!/bin/bash
#PBS -N kraken
#PBS -l select=1:ncpus=20:mem=350gb:scratch_local=10gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add kraken2-1.2

kraken2DB='/storage/brno3-cerit/home/kika/databases/kraken2DB'
datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/20xx0821_BML-B-first/'

#copy files to scratch
cp $datadir'1-reads/BML_trimmed_1.fq.gz' $SCRATCHDIR
cp $datadir'1-reads/BML_trimmed_2.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

fwd='BML_trimmed_1.fq.gz'
rev='BML_trimmed_2.fq.gz'
# assembly='bml_meta.spades_def.fa'
classified='BML_trimmed.classified.fq'
unclassified='BML_trimmed.unclassified.fq'
out='bml_reads.kraken.out'
report='bml_reads.kraken.report'


#on reads
kraken2 --db $kraken2DB --threads $PBS_NUM_PPN \
  --classified-out $classified \
  --unclassified-out $unclassified \
  --report $report \
  --paired --gzip-compressed $fwd $rev > $out


# #on assembly
# kraken2 --db $kraken2DB --threads $PBS_NUM_PPN \
#   --classified-out $classified \
#   --unclassified-out $unclassified \
#   --report $report $assembly > $out

#copy files back
# rm $assembly
rm $fwd $rev
cp -R * $datadir'6b-kraken2_reads/'
