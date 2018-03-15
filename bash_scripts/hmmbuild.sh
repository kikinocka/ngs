#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/pt_division/'
msa=$sdir'dnaJ_PF00226_seed.txt'
out_hmm=$sdir'dnaJ_profile.hmm'
name='dnaJ'
summary=$sdir'dnaJ_build.out'
threads=4

hmmbuild -n $name -o $summary --amino --cpu $threads $out_hmm $msa