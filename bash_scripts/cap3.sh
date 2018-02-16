#!/bin/sh

cap3='/home/kika/programs/CAP3/cap3'
infile='/home/kika/MEGAsync/diplonema_mt/1621/genome_assembly/1621_DNA_scaffolds_filtered.fasta'
outfile='/home/kika/MEGAsync/diplonema_mt/1621/genome_assembly/1621_DNA_scaffolds_filtered_cap3.out'

$cap3 $infile > $outfile