#!/bin/sh

f='/home/kika/ownCloud/pelomyxa/genome_assembly/pelo_spades.fasta'
output='/home/kika/ownCloud/pelomyxa/genome_assembly/quast/pelo_spades_all/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
