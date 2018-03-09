#!/bin/sh

infile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/sec/secA/secA.fa'
outfile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/sec/secA/secA_mafft.fa'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile