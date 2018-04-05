#!/bin/sh

cap3='/home/kika/tools/CAP3/cap3'
infile='/home/kika/diplonema/genome_assembly/1621/spades/scaffolds.fasta'
outfile='/home/kika/diplonema/genome_assembly/1621/cap3/1621_cap3.out'

$cap3 $infile > $outfile