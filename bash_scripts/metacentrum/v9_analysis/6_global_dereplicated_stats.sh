#!/bin/bash

raw='/storage/brno3-cerit/home/kika/sl_euglenozoa/'
fasta=$raw'global_dereplicated.fa'

cd $raw
# if [ $# != 1 ]; then
#     echo "You need to supply an input filename";
#     exit 1;
# fi

echo "Unique Seqs | Raw Reads"
awk -F "[;=]" '/^>/ {s += $3 ; c += 1} END {print s, c}' $fasta
