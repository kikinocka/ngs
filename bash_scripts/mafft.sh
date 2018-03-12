#!/bin/sh

infile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/srp/HMM/ftsy.txt'
outfile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/srp/HMM/ftsy_mafft.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile