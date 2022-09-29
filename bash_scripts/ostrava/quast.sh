#!/bin/bash
#PBS -N quast
#PBS -l nodes=1:ppn=20
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe


assembly='/mnt/data/kika/blastocrithidia/o_modryi/spades_75_karect/contigs.fasta'
out='/mnt/data/kika/blastocrithidia/o_modryi/spades_75_karect/quast/contigs/'

quast.py -o $out -t 20 $assembly
