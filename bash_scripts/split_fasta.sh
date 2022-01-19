#!/bin/bash

workdir='/Users/kika/ownCloud/archamoebae/DNA_maintenance/replisome_amoebae/targeting/'
seqs=$workdir'replisome_proteins.fa'

cd $workdir
awk 'BEGIN {n_seq=0;} /^>/ {if(n_seq%100==0){file=sprintf("myseq%d.fa",n_seq);} print >> file; n_seq++; next;} \
{ print >> file; }' < $seqs
