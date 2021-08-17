#!/bin/bash
#PBS -N kraken
#PBS -l select=1:ncpus=20:mem=350gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add kraken2-1.2

kraken2DB='/storage/brno3-cerit/home/kika/databases/kraken2DB'
datadir='/auto/brno3-cerit/nfs4/home/kika/oil_sands/metagenomes/P3B_1-06D_L001-ds.435324be81dc4260a8e3e8dbb5ed960c//'

#copy files to scratch
# cp $datadir'1-reads/BML_trimmed_1.fq.gz' $SCRATCHDIR
# cp $datadir'1-reads/BML_trimmed_2.fq.gz' $SCRATCHDIR
cp $datadir'2-spades/scaffolds.fasta' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

# fwd='BML_trimmed_1.fq.gz'
# rev='BML_trimmed_2.fq.gz'
assembly='scaffolds.fasta'
classified='P3B.classified.fa'
unclassified='P3B.unclassified.fa'
out='P3B.kraken.out'
report='P3B.kraken.report'


# #on reads
# kraken2 --db $kraken2DB --threads $PBS_NUM_PPN \
#   --classified-out $classified \
#   --unclassified-out $unclassified \
#   --report $report \
#   --paired --gzip-compressed $fwd $rev > $out

#on assembly
kraken2 --db $kraken2DB --threads $PBS_NUM_PPN \
  --classified-out $classified \
  --unclassified-out $unclassified \
  --report $report $assembly > $out

#copy files back
# rm $fwd $rev
rm $assembly
cp -R * $datadir'4-kraken2_assembly/'
