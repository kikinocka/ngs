#!/bin/bash

workdir='/Users/kika/ownCloud/blasto_comparative/genomes/'
seqs=$workdir'Oeli_genome_final_masked.fa'

cd $workdir
awk 'BEGIN {n_seq=0;} /^>/ {if(n_seq%3000==0){file=sprintf("myseq%d.fa",n_seq);} print >> file; n_seq++; next;} \
{ print >> file; }' < $seqs
