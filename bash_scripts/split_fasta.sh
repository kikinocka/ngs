#!/bin/bash

workdir='/Users/kika/ownCloud/SL_Euglenozoa/V9/euglenozoa/v9/'
seqs=$workdir'v9.fa'

cd $workdir
awk 'BEGIN {n_seq=0;} /^>/ {if(n_seq%1000==0){file=sprintf("v9_%d.fa",n_seq);} print >> file; n_seq++; next;} \
{ print >> file; }' < $seqs
