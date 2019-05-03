#!/bin/sh

cd /home/kika/work_dir/
infile='1621_contigs.fa'
outfile='1621_contigs_MAFFT.aln'

mafft --thread 32 --threadit 0 --inputorder --auto $infile > $outfile