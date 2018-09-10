#!/bin/bash

db='/home/kika/diplo_mt/transcriptomes/1604-Trinity2.fasta'
sdir='/home/kika/MEGAsync/diplonema_mt/HMM/'
hmm_prof=$sdir'y5-m3_profile.hmm'
output=$sdir'1604_y5-m3_hmm.out'
threads=4

hmmsearch -o $output --cpu $threads $hmm_prof $db