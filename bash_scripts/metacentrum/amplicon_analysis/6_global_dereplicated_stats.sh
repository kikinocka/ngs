#!/bin/bash

data='/storage/brno3-cerit/home/kika/oil_sands/18S-V4-2018/'
fasta=$data'global_dereplicated.fa'
out=$data'global.stats.txt'

cd $data
# if [ $# != 1 ]; then
#     echo "You need to supply an input filename";
#     exit 1;
# fi

echo 'I am in: ' `pwd`
echo 'Running global stats on: ' $fasta
echo "Unique Seqs | Raw Reads" > $out
awk -F "[;=]" '/^>/ {s += $3 ; c += 1} END {print s, c}' $fasta >> $out
echo 'awk done'
echo '******************'
