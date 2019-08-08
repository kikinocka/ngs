#!/bin/sh

cd /home/kika/ownCloud/lmex_mutants/eep_ko/
infile='ko2_EEP.fasta'
outfile='ko2_EEP.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile
