#!/bin/bash
#PBS -N kraken
#PBS -l select=1:ncpus=20:mem=150gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add kraken2-1.0

db_dir='/storage/brno3-cerit/home/kika/databases/kraken2'
datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/'

#copy files to scratch
cp $datadir'bml_meta.spades_def.fa' $SCRATCHDIR
cp $db_dir'/'* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

assembly='bml_meta.spades_def.fa'
out='bml_meta.kraken.out'
report='bml_meta.kraken.report'

kraken2 --db kraken2-db --threads $PBS_NUM_PPN --report $report $assembly > $out


kraken2 -db kraken2-db --threads 16 --report SRR1957167.fastq.report --unclassified-out SRR1957167.fastqunclassified#.fq --classified-out SRR1957167.fastq.fastqclassified#.fq --paired /home/pip17/scratch/giardia_pop_genomics/paired_reads_all_projects/SRR1957167/SRR1957167_1.fastq /home/pip17/scratch/giardia_pop_genomics/paired_reads_all_projects/SRR1957167/SRR1957167_2.fastq > SRR1957167.fastq.Kraken.out

Options:
  --db NAME               Name for Kraken 2 DB
                          (default: none)
  --threads NUM           Number of threads (default: 1)
  --quick                 Quick operation (use first hit or hits)
  --unclassified-out FILENAME
                          Print unclassified sequences to filename
  --classified-out FILENAME
                          Print classified sequences to filename
  --output FILENAME       Print output to filename (default: stdout); "-" will
                          suppress normal output
  --confidence FLOAT      Confidence score threshold (default: 0.0); must be
                          in [0, 1].
  --minimum-base-quality NUM
                          Minimum base quality used in classification (def: 0,
                          only effective with FASTQ input).
  --report FILENAME       Print a report with aggregrate counts/clade to file
  --use-mpa-style         With --report, format report output like Kraken 1s
                          kraken-mpa-report
  --report-zero-counts    With --report, report counts for ALL taxa, even if
                          counts are zero
  --memory-mapping        Avoids loading database into RAM
  --paired                The filenames provided have paired-end reads
  --use-names             Print scientific names instead of just taxids
  --gzip-compressed       Input files are compressed with gzip
  --bzip2-compressed      Input files are compressed with bzip2
  --help                  Print this message
  --version               Print version information


#copy files back
rm $assembly
cp -R * $datadir'kraken2'
