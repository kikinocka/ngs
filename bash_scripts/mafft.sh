#!/bin/sh

infile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Fd+FNR/Sulfite_reductase/CysJ.fa'
outfile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Fd+FNR/Sulfite_reductase/CysJ.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile