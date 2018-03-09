#!/bin/bash

sdir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/sec/secY/HMM/'
hmm_prof=$sdir'scy2_profile.hmm'
db='/home/kika/MEGAsync/Data/Eutreptiella/Eutreptiella_gymnastica_CCMP1594_MMETSP0810.fasta'
output=$sdir'ccmp_scy2_search.out'
threads=4

hmmsearch -o $output --cpu $threads $hmm_prof $db