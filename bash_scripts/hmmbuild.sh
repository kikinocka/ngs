#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Ribosomal_Proteins/L24/'
msa=$sdir'PF17136_seed.txt'
out_hmm=$sdir'L24_profile.hmm'
name='L24'
summary=$sdir'L24_build.out'
threads=4

hmmbuild -n $name -o $summary --amino --cpu $threads $out_hmm $msa