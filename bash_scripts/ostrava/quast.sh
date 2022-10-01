#!/bin/bash
#PBS -N quast
#PBS -l nodes=1:ppn=20
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe


assembly='/mnt/data/kika/blastocrithidia/b_spHR05/spades_75_careful/scaffolds.fasta'
out='/mnt/data/kika/blastocrithidia/b_spHR05/spades_75_careful/quast/scaffolds/'

quast.py -o $out -t 20 $assembly
