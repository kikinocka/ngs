#!/bin/sh

cap3='/home/kika/tools/CAP3/cap3'
infile='/home/kika/diplonema/genome_assembly/1604_cap3/1604_DNA_scaffolds_filtered.fasta'
outfile='/home/kika/diplonema/genome_assembly/1604_cap3/1604_DNA_scaffolds_filtered_cap3.out'

cap3 $infile > $outfile