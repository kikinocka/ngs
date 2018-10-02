#!/bin/sh

f='/home/kika/MEGAsync/pelomyxa/genome_assembly/p1_scaffolds.fasta'
output='/home/kika/MEGAsync/pelomyxa/genome_assembly/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
