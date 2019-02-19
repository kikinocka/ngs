#!/bin/sh

f='/home/kika/ownCloud/pelomyxa/genome_assembly/pelomyxa_clean.fa'
output='/home/kika/ownCloud/pelomyxa/genome_assembly/quast/pelomyxa_clean/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
