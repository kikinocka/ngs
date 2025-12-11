#!/bin/sh

quast='/Users/kika/miniconda3/bin/quast.py'

cd '/Users/kika/ownCloud/Euglena_gracilis/genome/hifi/'
assembly='EG_hifi.asm_default.p_ctg.fa'
output='quast/default/'

python $quast --eukaryote -o $output -t 6 $assembly
