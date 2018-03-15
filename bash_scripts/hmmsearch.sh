#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/pt_division/'
hmm_prof=$sdir'dnaJ_profile.hmm'
db='/home/kika/MEGAsync/Data/EG_RNAseq/EGALL_6frames.fasta'
output=$sdir'eg_dnaJ_search.out'
threads=4

hmmsearch -o $output --cpu $threads $hmm_prof $db