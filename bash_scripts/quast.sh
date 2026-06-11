#!/bin/sh

quast='/Users/kika/miniconda3/bin/quast.py'

cd '/Users/kika/Downloads/'
assembly='GCA_039621445.1_ASM3962144v1_genomic.fna'
output='quast/'

python $quast --eukaryote -o $output -t 6 $assembly
