#!/bin/sh

f='/home/kika/MEGAsync/diplonema_mt/1618/genome_assembly/1618_DNA_scaffolds.fasta'
output='/home/kika/MEGAsync/diplonema_mt/1618/genome_assembly/quast/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
