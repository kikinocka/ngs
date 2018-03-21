#!/bin/sh

f='/home/kika/diplo_genomes/1601_contigs.fa'
output='/home/kika/diplo_genomes/quast/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
