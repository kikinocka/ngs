#!/bin/sh

cd /home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/pyruvate_metabolism/hydA_tree/
infile='hydA_seqs.fa'
outfile='hydA_MAFFT.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile