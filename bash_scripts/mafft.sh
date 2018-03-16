#!/bin/sh

infile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Rho_factor/nr70/nr70.fa'
outfile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Rho_factor/nr70/nr70_mafft.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile