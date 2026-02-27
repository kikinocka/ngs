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
datadir='/storage/brno12-cerit/home/kika/blasto_comparative/triatomae/genome_reads/'

#copy files to scratch
cp $datadir'triat_trimmed_1.fq' $SCRATCHDIR
cp $datadir'triat_trimmed_2.fq' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

fwd='triat_trimmed_1.fq'
rev='triat_trimmed_2.fq'
classified='Ag83.classified#.fq'
unclassified='Ag83.unclassified#.fq'
out='Ag83.kraken.out'
report='Ag83.kraken.report'
krona='Ag83.krona.html'

#on reads
kraken2 --db $kraken2DB --threads $PBS_NUM_PPN \
  --classified-out $classified \
  --unclassified-out $unclassified \
  --report $report \
  --paired --gzip-compressed $fwd $rev > $out

ImportTaxonomy.pl -m $PBS_NUM_PPN -t 5 $report -o $krona


#copy files back
rm $fwd $rev
cp -R * '/storage/brno12-cerit/home/kika/pkld/kraken2/test/'
