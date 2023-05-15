#!/bin/sh

quast='/Users/kika/miniconda3/bin/quast.py'

cd '/Users/kika/ownCloud/amoebophrya/'
assembly='scaffolds.fasta'
output='quast/'

python $quast --eukaryote -o $output -t 4 $assembly
