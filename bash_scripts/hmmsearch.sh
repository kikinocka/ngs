#!/bin/bash

db='/home/kika/ownCloud/pelomyxa/transcriptome_assembly/pelomyxa_trinity_translated.fasta'
sdir='/home/kika/ownCloud/pelomyxa/mito_proteins/complexII/'
hmm_prof=$sdir'aox_pfam_profile.hmm'
output=$sdir'pelo_aox_pfam_hmm.out'
threads=4

hmmsearch -o $output --cpu $threads $hmm_prof $db
