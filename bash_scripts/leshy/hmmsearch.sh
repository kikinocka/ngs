#!/bin/bash

cd '/mnt/mokosz/home/kika/mito_import_HMMs/'

db='/mnt/mokosz/home/kika/eukprot_amoebozoa/amoebozoa.fa'
orgn='eukprot_amoebozoa'

for profile in *.hmm ; do
	echo $profile
	output=$orgn'_'${profile%.hmm}.hmm_search.table
	threads=10
	hmmsearch --tblout $output --cpu $threads $profile $db
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py HMMsearch done
