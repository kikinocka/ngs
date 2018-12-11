#!/bin/sh

cd /home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Fd+FNR/chlamydial/
infile='fd_seqs.fa'
outfile='fd_MAFFT.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile