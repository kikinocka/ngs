#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/sec/secY/HMM/'
msa=$sdir'scy2_mafft.fa'
out_hmm=$sdir'scy2_profile.hmm'
name='scy2'
summary=$sdir'scy2_build.out'
threads=4

hmmbuild -n $name -o $summary --amino --cpu $threads $out_hmm $msa