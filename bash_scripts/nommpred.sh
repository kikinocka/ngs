#!/bin/sh

workdir='/mnt/mokosz/home/kika/'
input=$workdir'diplo_all.fa'
out=$workdir'diplo_all.nommpred.out'
lineage=1
# 1) Mt
# 2) MRO
# 3) Piroplasma
# 4) Chlorophyta
# 5) Dictyostelium
# 6) Plasmodium
# 7) stramenopiles
# 8) Toxoplasma
# 9) Trypanosomatida

NommPred.py -i $input -l $lineage #-o $out --overwrite
