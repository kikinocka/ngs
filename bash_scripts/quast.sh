#!/bin/sh

f='/home/kika/ownCloud/pelomyxa/genome_assembly/p2_scaffolds.fasta'
output='/home/kika/ownCloud/pelomyxa/genome_assembly/quast/p2/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
