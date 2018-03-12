#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/srp/HMM/'
msa=$sdir'srp54_mafft.aln'
out_hmm=$sdir'srp54_profile.hmm'
name='srp54'
summary=$sdir'srp54_build.out'
threads=4

hmmbuild -n $name -o $summary --amino --cpu $threads $out_hmm $msa