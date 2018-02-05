#!/bin/bash

sdir='/home/kika/MEGAsync/blasto_project/genes/repair/NHEJ/'
msa=$sdir'ku_PF02735_seed.txt'
out_hmm=$sdir'ku_profile.hmm'
name='ku'
summary=$sdir'ku_build.out'
threads=4

hmmbuild -n $name -o $summary --amino --cpu $threads $out_hmm $msa