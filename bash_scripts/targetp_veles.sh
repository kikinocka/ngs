#!/bin/bash

targetp='/home/kika/tools/targetp-1.1/targetp'
workdir='/home/kika/pelomyxa_schiedti/predicted_proteins/'
infile=$workdir'pelo_transcriptome_clean.fa.transdecoder.5prime_complete.clustered.pep'
outfile=$workdir'pelo_transcriptome_clean.fa.transdecoder.5prime_complete.clustered.targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
