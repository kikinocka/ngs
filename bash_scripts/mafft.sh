#!/bin/sh

infile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/FTSH_proteases/FTSH_proteases_phylogeny.txt'
outfile='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/FTSH_proteases/FTSH_mafft.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile