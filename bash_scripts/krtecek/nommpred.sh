#!/bin/sh

nommpred='/home/software/NommPred/NommPred.py'

workdir='/home/users/kika/diplonema/predictions/'
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

python3 $nommpred -i $input -o $out -l $lineage --overwrite
