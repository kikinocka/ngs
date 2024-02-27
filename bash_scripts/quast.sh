#!/bin/sh

quast='/Users/kika/miniconda3/bin/quast.py'

cd '/Users/kika/ownCloud/blastocrithidia/genome_assembly/'
assembly='p57_polished.fa'
output='quast/p57_polished2/'

python $quast --eukaryote -o $output -t 6 $assembly
