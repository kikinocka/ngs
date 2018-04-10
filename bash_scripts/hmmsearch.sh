#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/tat/HMM/'
hmm_prof=$sdir'tatC_profile.hmm'
db='/home/kika/MEGAsync/Data/EL_RNAseq/20140707_ver._r2013-02-05/el_merged_translated.fasta'
output=$sdir'el_tatC_search.out'
threads=4

hmmsearch -o $output --cpu $threads $hmm_prof $db