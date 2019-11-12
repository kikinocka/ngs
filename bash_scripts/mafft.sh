#!/bin/sh

cd /home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Tetrapyrroles/precorrin-2_dehydrogenase/
infile='SDR_a4_aa.fa'
outfile='SDR_a4_mafft.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile
