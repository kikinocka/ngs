#!/bin/bash
#PBS -N kraken
#PBS -l select=1:ncpus=20:mem=350gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add kraken2-1.2
module add krona-2.8

kraken2DB='/storage/brno3-cerit/home/kika/databases/kraken2DB-eukprot'
datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P1B_1-05C_L001-ds.ec8b691bd68b44deb59919ca3da275ba/'

#copy files to scratch
# cp $datadir'1-reads/P1B_trimmed_1.fq.gz' $SCRATCHDIR
# cp $datadir'1-reads/P1B_trimmed_2.fq.gz' $SCRATCHDIR
cp $datadir'2-spades/scaffolds.fasta' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

# fwd='P1B_trimmed_1.fq.gz'
# rev='P1B_trimmed_2.fq.gz'
# classified='P1B.classified#.fq'
# unclassified='P1B.unclassified#.fq'
assembly='scaffolds.fasta'
classified='P1B.classified.fa'
unclassified='P1B.unclassified.fa'
out='P1B.kraken.out'
report='P1B.kraken.report'
krona='P1B.kraken.html'

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

ImportTaxonomy.pl -m $PBS_NUM_PPN -t 5 $report -o $krona


#copy files back
# rm $fwd $rev
rm $assembly
cp -R * $datadir'4c-kraken2-eukprot_assembly/'
