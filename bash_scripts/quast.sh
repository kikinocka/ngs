#!/bin/sh

f='/home/kika/MEGAsync/diplonema_mt/1604/1604_DNA_scaffolds.fasta'
output='/home/kika/MEGAsync/diplonema_mt/1604/quast'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
