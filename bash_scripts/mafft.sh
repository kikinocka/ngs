#!/bin/sh

cd '/home/kika/MEGAsync/diplonema/paramylon/phosphorylase/'
infile='GH149.fa'
outfile='GH149_mafft.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile
