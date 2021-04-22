#!/bin/sh

cd '/mnt/mokosz/home/kika/archam_trees/d-ldh'
infile='d-ldh.fa'
outfile='d-ldh.mafft.aln'
report='d-ldh.mafft.log'

mafft --thread 15 --localpair --maxiterate 1000 --inputorder $infile > $outfile 2> $report
