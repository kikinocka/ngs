#!/bin/sh

#align denovo
cd '/mnt/mokosz/home/kika/metamonads/MRO_proteins/2-MRO_fasta/'

fasta='TrxR.fa'
aln=${fasta%.fa}.mafft.aln
log=${fasta%.fa}.mafft.log

mafft --thread 15 --localpair --maxiterate 1000 --inputorder ${fasta} > ${aln} 2> ${log}

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MAFFT one done
