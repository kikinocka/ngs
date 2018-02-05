#!/bin/bash

sdir='/home/kika/MEGAsync/blasto_project/genes/repair/NHEJ/ku_pfam/'
hmm_prof=$sdir'ku_profile.hmm'
db='/home/kika/MEGAsync/blasto_project/genome_assembly/jaculum_scaffolds_transc_translated.fasta'
output=$sdir'ku_search_jac.out'
threads=4

hmmsearch -o $output --cpu $threads $hmm_prof $db