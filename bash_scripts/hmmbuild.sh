#!/bin/bash

sdir='/home/kika/MEGAsync/diplonema/paramylon/phosphorylase/'
msa=$sdir'GH149_mafft.aln'
out_hmm=$sdir'GH149_profile.hmm'
name='GH149'
summary=$sdir'GH149_build.out'
seq_type=amino
threads=4

hmmbuild -n $name -o $summary --$seq_type --cpu $threads $out_hmm $msa
