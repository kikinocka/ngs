#!/bin/bash
#PBS -N kraken2
#PBS -l select=1:ncpus=20:mem=900gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module load kraken2
module add krona-2.8

kraken2DB='/storage/projects-du-praha/Bio_databases/kraken2/kraken2_nt_20240530'
datadir='/storage/brno12-cerit/home/kika/pkld/'

#copy files to scratch
cp $datadir'trimmed_all/karect_Ag83_trimmed_1.fq.gz' $SCRATCHDIR
cp $datadir'trimmed_all/karect_Ag83_trimmed_2.fq.gz' $SCRATCHDIR
# cp $datadir'2-spades/scaffolds.fasta' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

fwd='karect_Ag83_trimmed_1.fq.gz'
rev='karect_Ag83_trimmed_2.fq.gz'
classified='Ag83.classified#.fq'
unclassified='Ag83.unclassified#.fq'
# assembly='scaffolds.fasta'
# classified='P1B.classified.fa'
# unclassified='P1B.unclassified.fa'
out='Ag83.kraken.out'
report='Ag83.kraken.report'
krona='Ag83.krona.html'

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

ImportTaxonomy.pl -m $PBS_NUM_PPN -t 5 $report -o $krona


#copy files back
rm $fwd $rev
# rm $assembly
cp -R * $datadir'kraken2/'
