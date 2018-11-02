#!/bin/sh

f='/home/kika/ownCloud/pelomyxa/transcriptome_assembly/pelo_schiedti_trinity.fasta'
output='/home/kika/ownCloud/pelomyxa/transcriptome_assembly/quast/pelo_all/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
