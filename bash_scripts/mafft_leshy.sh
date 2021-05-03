#!/bin/sh

cd '/mnt/mokosz/home/kika/archam_trees/ak/ver2/'
infile='ak.fa'
outfile='ak.mafft.aln'
report='ak.mafft.log'

mafft --thread 15 --localpair --maxiterate 1000 --inputorder $infile > $outfile 2> $report
