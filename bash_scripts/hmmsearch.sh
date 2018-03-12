#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/srp/HMM/'
hmm_prof=$sdir'ftsy_profile.hmm'
db='/home/kika/MEGAsync/Data/EG_RNAseq/EGALL_6frames.fasta'
output=$sdir'eg_ftsy_search.out'
threads=4

hmmsearch -o $output --cpu $threads $hmm_prof $db