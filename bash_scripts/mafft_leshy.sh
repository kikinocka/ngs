#!/bin/sh

cd '/mnt/mokosz/home/kika/archam_trees/pfl/ver2/'
infile='pfl.fa'
outfile='pfl.mafft.aln'
report='pfl.mafft.log'

mafft --thread 15 --localpair --maxiterate 1000 --inputorder $infile > $outfile 2> $report
