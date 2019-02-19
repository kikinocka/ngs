#!/bin/sh

cd /home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Glycerolipids/SQD_pathway/SQD2_tree/
infile='sqd2.fasta'
outfile='sqd2_MAFFT.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile