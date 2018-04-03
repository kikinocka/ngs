#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Ribosomal_Proteins/L24/'
hmm_prof=$sdir'L24_profile.hmm'
db='/home/kika/MEGAsync/Data/Eutreptiella/Eutreptiella_gymnastica_NIES-381.fasta'
output=$sdir'nies_L24_search.out'
threads=4

hmmsearch -o $output --cpu $threads $hmm_prof $db