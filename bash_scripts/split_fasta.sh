#!/bin/bash

workdir='/Users/kika/ownCloud/oil_sands/amplicons/18S-V4-2018/filtration/'
seqs=$workdir'check_cont2.fa'

cd $workdir
awk 'BEGIN {n_seq=0;} /^>/ {if(n_seq%100000==0){file=sprintf("myseq%d.fa",n_seq);} print >> file; n_seq++; next;} \
{ print >> file; }' < $seqs
