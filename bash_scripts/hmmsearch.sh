#!/bin/bash

db='/home/kika/diplo_mt/translated_genomes/1601_DNA_scaffolds_translated.fasta'
sdir='/home/kika/MEGAsync/diplonema_mt/HMM/'
hmm_prof=$sdir'y5-m2-3_profile.hmm'
output=$sdir'1601_y5-m2-3_hmm.out'
threads=4

hmmsearch -o $output --cpu $threads $hmm_prof $db