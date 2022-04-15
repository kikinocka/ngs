#!/bin/sh

quast='/Users/kika/miniconda3/bin/quast.py'

cd '/Users/kika/ownCloud/blastocrithidia/transcriptome_assembly/new_3-UTR/'
assembly='Trinity.fasta'
output='quast/'

python $quast --eukaryote -o $output -t 4 $assembly
