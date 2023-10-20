#!/bin/sh

quast='/Users/kika/miniconda3/bin/quast.py'

cd '/Users/kika/ownCloud/oil_sands/metagenomes/20210222_BML-P3S/2-spades/'
assembly='P3S_scaffolds.fasta'
output='/Users/kika/ownCloud/oil_sands/metagenomes/20210222_BML-P3S/3-quast'

python $quast --eukaryote -o $output -t 6 $assembly
