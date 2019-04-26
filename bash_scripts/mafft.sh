#!/bin/sh

cd /home/kika/ownCloud/pelomyxa/mito_proteins/complexII/
infile='amoebozoa_aox.fasta'
outfile='amoebozoa_aox_MAFFT.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile