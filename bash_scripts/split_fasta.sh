#!/bin/bash

workdir='/Users/kika/ownCloud/Euglena_gracilis/genome/hifi/'
seqs=$workdir'EG_hifi.asm.p_ctg.fasta'

cd $workdir
awk 'BEGIN {n_seq=0;} /^>/ {if(n_seq%1000==0){file=sprintf("EG_%d.fasta",n_seq);} print >> file; n_seq++; next;} \
{ print >> file; }' < $seqs
