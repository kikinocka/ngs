#!/bin/bash

cd '/mnt/mokosz/home/kika/tom60/'

db='/mnt/mokosz/home/zoli/DMND/EukProt_v2_renamed.faa'

for profile in *.hmm_profile ; do:
	output=${profile%.hmm_profile}.hmm_search.out
	threads=10
	hmmsearch -o $output --cpu $threads $profile $db
done
