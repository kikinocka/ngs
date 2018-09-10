#!/bin/bash

sdir='/home/kika/MEGAsync/diplonema_mt/HMM/'
msa=$sdir'y5-m3.fasta'
out_hmm=$sdir'y5-m3_profile.hmm'
name='y5-m3'
summary=$sdir'y5-m3_build.out'
seq_type=dna
threads=4

hmmbuild -n $name -o $summary --$seq_type --cpu $threads $out_hmm $msa