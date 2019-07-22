#!/bin/sh

cd /home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/fes_cluster_assembly/nif/nifU_tree/domain/
infile='nifU_seqs.fa'
outfile='nifU_MAFFT.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile
