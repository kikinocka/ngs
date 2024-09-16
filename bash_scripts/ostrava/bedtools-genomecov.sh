#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N bedtools-genomecov
#PBS -l nodes=1:ppn=20
#PBS -l walltime=100:00:00


cd '/home/users/kika/bnon_KOs/catalase/bw2_mapping/'

genome='/home/users/kika/bnon_KOs/p57_polished.fa'
bamfile='cat_KO.bw2_sorted.bam'
out='cat_KO.genomecov.tsv'

# bedtools genomecov -d -split -ibam $bamfile -g $genome > $out
bedtools genomecov -bga -split -ibam $bamfile -g $genome > $out

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: bedtools genome coverage done
