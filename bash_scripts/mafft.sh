#!/bin/sh

infile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/sec/secY/secY.fa'
outfile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/sec/secY/secY_mafft.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile