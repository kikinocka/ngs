#!/bin/sh

f='/home/kika/ownCloud/pelomyxa/genome_assembly/p4_scaffolds_k127.fasta'
output='/home/kika/ownCloud/pelomyxa/genome_assembly/quast/p4_k127/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
