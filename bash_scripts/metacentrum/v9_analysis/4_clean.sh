#!/bin/bash

raw='/storage/brno3-cerit/home/kika/sl_euglenozoa/raw_reads/'
trimmed='/storage/brno3-cerit/home/kika/sl_euglenozoa/trimmed_cutadapt/'

# # compress
# cd $raw
# for f in *_001.fastq ; do
#     bzip2 -9 ${f}
# done &

# # clean
# rm *.assembled.{log,fastq}

# rename
cd $trimmed
for f in *.assembled.fasta ; do
    mv ${f} ${f/.assembled.fasta/.fas}
done
