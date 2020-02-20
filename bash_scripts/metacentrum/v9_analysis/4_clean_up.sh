#!/bin/bash

raw='/storage/brno3-cerit/home/kika/sl_euglenozoa/raw_reads/'
merged='/storage/brno3-cerit/home/kika/sl_euglenozoa/merged_pear/'
trimmed='/storage/brno3-cerit/home/kika/sl_euglenozoa/trimmed_cutadapt/'

# compress
cd $raw
for f in *.fastq ; do
    bzip2 -9 ${f}
done &

cd $merged
for f in *.fastq ; do
    bzip2 -9 ${f}
done &

# # clean
# rm *.assembled.{log,fastq}

# rename
cd $trimmed
for f in *.fas ; do
    mv ${f} ${f/.fas/.assembled.fasta}
done
