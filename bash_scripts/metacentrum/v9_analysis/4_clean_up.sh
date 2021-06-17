#!/bin/bash

data='/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/'
raw=$data'raw_reads/'
merged=$data'merged_pear/'
trimmed=$data'trimmed_cutadapt/'

# # compress
# cd $raw
# echo 'I am in: ' $pwd
# for f in *.fastq ; do
# 	echo 'Compressing: ' $f
#     bzip2 -9 ${f}
# done &

cd $merged
echo 'I am in: ' $pwd
for f in *.fastq ; do
	echo 'Compressing: ' $f
    bzip2 -9 ${f}
done &

# # clean
# rm *.assembled.{log,fastq}

# rename
cd $trimmed
echo 'I am in: ' $pwd
for f in *.assembled.fasta ; do
	echo 'Renaming: ' $f
    mv ${f} ${f/.assembled.fasta/.fas}
done
