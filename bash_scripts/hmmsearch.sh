#!/bin/bash

sdir='/home/kika/MEGAsync/blasto_project/genes/repair/NHEJ/ku80_hmmer/'
hmm_prof=$sdir'ku80_profile.hmm'
db='/home/kika/MEGAsync/blasto_project/genome_assembly/jaculum_scaffolds_transc_translated.fasta'
output=$sdir'ku80_search_jac.out'
threads=4

hmmsearch -o $output --cpu $threads $hmm_prof $db