#!/bin/sh

cd '/mnt/mokosz/home/kika/archam_trees/pfo/'
infile='pfo.fa'
outfile='pfo.mafft.aln'
report='pfo.mafft.log'

mafft --thread 15 --localpair --maxiterate 1000 --inputorder $infile > $outfile 2> $report
