#!/bin/sh

cd '/Dcko/ownCloud/proteromonas/PXMP2_tree/'
infile='pxmp2.fa'
outfile='pxmp2.mafft.aln'

mafft --thread 4 --threadit 0 --maxiterate 100 --inputorder --auto $infile > $outfile
