#!/bin/sh

cd /home/kika/MEGAsync/diplonema_paramylon/beta-1,3-glucan_synthase/domain/
infile='glucane_synthase_seqs.fasta'
outfile='glucane_synthase_MAFFT.aln'

mafft --thread 4 --threadit 0 --inputorder --auto $infile > $outfile