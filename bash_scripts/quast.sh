#!/bin/sh

f='/home/kika/ownCloud/blastocrithidia/genome_assembly/jaculum_scaffolds_transc.fasta'
output='/home/kika/ownCloud/blastocrithidia/genome_assembly/quast/jaculum_scaffolds_transc/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
