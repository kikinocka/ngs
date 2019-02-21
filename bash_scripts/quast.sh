#!/bin/sh

f='/home/kika/ownCloud/pelomyxa/genome_assembly/pelo_clean_rascaf.fa'
output='/home/kika/ownCloud/pelomyxa/genome_assembly/quast/pelomyxa_clean_rascaf/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
