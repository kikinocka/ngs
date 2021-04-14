#!/bin/sh

cd '/mnt/mokosz/home/kika/archam_trees/pfla/'
infile='pfla.fa'
outfile='pfla.mafft.aln'
report='pfla.mafft.log'

mafft --thread 15 --localpair --maxiterate 1000 --inputorder $infile > $outfile 2> $report
