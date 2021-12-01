#!/bin/bash

cd '/mnt/mokosz/home/kika/tom60/'

db='/mnt/mokosz/home/zoli/DMND/EukProt_v2_renamed.faa'
orgn='eukprot_'

for profile in *.hmm_profile ; do
	echo $profile
	output=$orgn${profile%.hmm_profile}.hmm_search.table
	threads=10
	hmmsearch --tblout $output --cpu $threads $profile $db
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py HMMsearch done
