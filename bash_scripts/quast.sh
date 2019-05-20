#!/bin/sh

f='/home/kika/ownCloud/blastocrithidia/genome_assembly/lmex_ku80.fa'
output='/home/kika/ownCloud/blastocrithidia/genome_assembly/quast/lmex_ku80/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
