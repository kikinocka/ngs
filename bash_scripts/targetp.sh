#!/bin/bash

targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/ownCloud/pelomyxa_schiedti/predicted_proteins/'
infile=$workdir'pelomyxa_transcriptome_clean.fa.transdecoder.5prime_complete.clustered.pep'
outfile=$workdir'proteins_targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
