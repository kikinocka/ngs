#!/bin/sh

infile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/TOC-TIC/2nd_iter/tic55.fas'
outfile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/TOC-TIC/2nd_iter/tic55_mafft.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile