#!/bin/bash

workdir='/home/kika/MEGAsync/Data/dpapilatum/'
seqs=$workdir'dpap_peroxisomal.fa'

cd $workdir
awk 'BEGIN {n_seq=0;} /^>/ {if(n_seq%1000==0){file=sprintf("myseq%d.fa",n_seq);} print >> file; n_seq++; next;} \
{ print >> file; }' < $seqs
