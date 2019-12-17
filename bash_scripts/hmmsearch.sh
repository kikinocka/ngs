#!/bin/bash

db='/home/kika/MEGAsync/Data/kinetoplastids/TriTrypDB-46_BsaltansLakeKonstanz_Genome_translated.fa'
sdir='/home/kika/MEGAsync/diplonema/paramylon/phosphorylase/'
hmm_prof=$sdir'GH149_profile.hmm'
output=$sdir'bsal_gen_GH149_hmm.out'
threads=4

hmmsearch -o $output --cpu $threads $hmm_prof $db
