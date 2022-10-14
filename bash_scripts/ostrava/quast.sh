#!/bin/bash
#PBS -N quast
#PBS -l nodes=1:ppn=20
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe


assembly='/mnt/data/kika/blastocrithidia/o_eliasi/genome_final/Oeliasi_gapClosed_Bojana.fasta'
out='/mnt/data/kika/blastocrithidia/o_eliasi/genome_final/quast/'

quast.py -o $out -t 20 $assembly
