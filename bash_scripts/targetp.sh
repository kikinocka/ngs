#!/bin/sh
targetp='/home/kika/programs/targetp-1.1/targetp'
infile='/home/kika/MEGAsync/Chlamydomonas/od_toma/putative_pt_genes_aa_complete5.fa'
outfile='/home/kika/MEGAsync/Chlamydomonas/od_toma/putative_pt_genes_aa_complete5_targetp.txt'
plant='P'
non_plant='N'

$targetp -$plant -c $infile > $outfile
