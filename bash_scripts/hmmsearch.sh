#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/TOC-TIC/2nd_iter/'
hmm_prof=$sdir'tic55_profile.hmm'
db='/home/kika/MEGAsync/Data/EL_RNAseq/20140707_ver._r2013-02-05/el_merged_translated.fasta'
output=$sdir'el_tic55_search.out'
threads=4

hmmsearch -o $output --cpu $threads $hmm_prof $db