#!/bin/sh

f='/home/kika/ownCloud/pelomyxa/genome_assembly/p1_scaffolds_k127.fasta'
output='/home/kika/ownCloud/pelomyxa/genome_assembly/quast/p1_k127/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
