#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Ribosomal_Proteins/S18/'
hmm_prof=$sdir'S18_profile.hmm'
db='/home/kika/MEGAsync/Data/Eutreptiella/Eutreptiella_gymnastica_CCMP1594_MMETSP0811.fasta'
output=$sdir'ccmp_11_S18_search.out'
threads=4

hmmsearch -o $output --cpu $threads $hmm_prof $db