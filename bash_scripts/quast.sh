#!/bin/sh

quast='/Users/kika/miniconda3/bin/quast.py'

cd '/Users/kika/ownCloud/Euglena_gracilis/genome/hifi/'
assembly='EG_hifi.asm_telomere.p_ctg.fa'
output='quast/telomere/'

python $quast --eukaryote -o $output -t 6 $assembly
