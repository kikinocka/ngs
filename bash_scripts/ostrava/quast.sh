#!/bin/bash
#PBS -N quast
#PBS -l nodes=1:ppn=20
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe


assembly='/mnt/data/bojana/Genomic/Obscuromonas_eliasi/Obscuromonas_eliasi_assembled/trimmed75_NOcareful/contigs.fasta'
out='/mnt/data/kika/blastocrithidia/o_eliasi/quast/trimmed75_nocorrection/contigs/'

quast.py -o $out -t 20 $assembly
