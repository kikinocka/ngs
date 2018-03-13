#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/TOC-TIC/2nd_iter/'
msa=$sdir'tic55_mafft.aln'
out_hmm=$sdir'tic55_profile.hmm'
name='tic55'
summary=$sdir'tic55_build.out'
threads=4

hmmbuild -n $name -o $summary --amino --cpu $threads $out_hmm $msa