#!/bin/sh

f='/home/kika/MEGAsync/diplonema_mt/1601/genome_assembly/1601_spades_guided_trusted.fasta'
output='/home/kika/MEGAsync/diplonema_mt/1601/genome_assembly/quast/spades_guided_trusted/'

/usr/bin/python3.5 /home/kika/programs/quast-4.4/quast.py $f -o $output -t 4
