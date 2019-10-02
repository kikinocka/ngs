#!/bin/bash

workdir='/home/kika/pelomyxa_schiedti/predicted_proteins/'
seqs=$workdir'pelo_transcriptome_clean.fa.transdecoder.5prime_complete.clustered.pep'

awk 'BEGIN {n_seq=0;} /^>/ {if(n_seq%1500==0){file=sprintf("myseq%d.fa",n_seq);} print >> file; n_seq++; next;} \
{ print >> file; }' < $seqs
