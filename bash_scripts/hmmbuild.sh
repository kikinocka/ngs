#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Ribosomal_Proteins/S18/'
msa=$sdir'PF01084_seed.txt'
out_hmm=$sdir'S18_profile.hmm'
name='S18'
summary=$sdir'S18_build.out'
threads=4

hmmbuild -n $name -o $summary --amino --cpu $threads $out_hmm $msa