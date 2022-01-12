#!/bin/bash

workdir='/Users/kika/ownCloud/archamoebae/ribosomal_proteins/amoebae/targeting/'
seqs=$workdir'ribosomal_proteins.fa'

cd $workdir
awk 'BEGIN {n_seq=0;} /^>/ {if(n_seq%100==0){file=sprintf("myseq%d.fa",n_seq);} print >> file; n_seq++; next;} \
{ print >> file; }' < $seqs
