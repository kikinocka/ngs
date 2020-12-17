#!/bin/sh

quast='/Users/kika/miniconda3/bin/quast.py'

cd '/Users/kika/ownCloud/SAGs/reassembly/'
assembly='EU1718_contigs_joined-FINAL.fa'
output='quast/'

python $quast --eukaryote -o $output -t 4 $assembly
