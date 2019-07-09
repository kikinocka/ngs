#!/bin/sh

cd /home/kika/MEGAsync/diplonema_paramylon/glucanase/
infile='glucanase.fa'
outfile='glucanase_MAFFT.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile
