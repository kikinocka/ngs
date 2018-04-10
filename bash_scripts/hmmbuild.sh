#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/tat/HMM/'
msa=$sdir'tatC.aln'
out_hmm=$sdir'tatC_profile.hmm'
name='tatC'
summary=$sdir'tatC_build.out'
threads=4

hmmbuild -n $name -o $summary --amino --cpu $threads $out_hmm $msa