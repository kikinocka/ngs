#!/bin/sh

cd '/mnt/mokosz/home/kika/archam_trees'
infile='acs.fa'
outfile='acs.mafft.aln'
report='acs.mafft.log'

mafft --thread 15 --localpair --maxiterate 1000 --inputorder $infile > $outfile 2> $report
