#!/bin/sh

cd /home/kika/MEGAsync/diplonema_catalase/
infile='catalase.fas'
outfile='catalase_MAFFT.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile
