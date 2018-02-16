#!/bin/sh

f='/home/kika/MEGAsync/diplonema_mt/1621/genome_assembly/cap3/1621_DNA_scaffolds_filtered_cap3.fa'
output='/home/kika/MEGAsync/diplonema_mt/1621/genome_assembly/cap3/quast/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
