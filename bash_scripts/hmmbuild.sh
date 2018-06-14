#!/bin/bash

sdir='/home/kika/MEGAsync/diplonema_mt/HMM/'
msa=$sdir'y5-m2-3.aln'
out_hmm=$sdir'y5-m2-3_profile.hmm'
name='y5-m2-3'
summary=$sdir'y5-m2-3_build.out'
seq_type=amino
threads=4

hmmbuild -n $name -o $summary --$seq_type --cpu $threads $out_hmm $msa