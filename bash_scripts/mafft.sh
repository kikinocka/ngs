#!/bin/sh

cd '/Dcko/ownCloud/proteromonas/ACSL_tree/ver2/'
infile='ACSL_seqs.fa'
outfile='ACSL.mafft.aln'

mafft --thread 4 --threadit 0 --maxiterate 100 --inputorder --auto $infile > $outfile
