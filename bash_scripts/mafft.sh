#!/bin/sh

cd '/Users/kika/ownCloud/SAGs/mit/phylogenomics/ver6/'
infile='nad9.fa'
outfile='nad9.mafft.aln'

mafft --thread 6 --threadit 0 --maxiterate 1000 --inputorder --auto $infile > $outfile
