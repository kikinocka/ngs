#!/bin/sh

workdir='/mnt/mokosz/home/kika/pelomyxa_schiedti/'
input=$workdir'pelo_others.fa'
out=$workdir'pelo_others.nommpred_mro.tsv'
lineage=2
# 1) Mt
# 2) MRO
# 3) Piroplasma
# 4) Chlorophyta
# 5) Dictyostelium
# 6) Plasmodium
# 7) stramenopiles
# 8) Toxoplasma
# 9) Trypanosomatida

NommPred.py -i $input -o $out -l $lineage --overwrite
