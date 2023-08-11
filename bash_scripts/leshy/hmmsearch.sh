#!/bin/bash

cd '/mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/'

db='/mnt/mokosz/home/kika/eukprot_amoebozoa/amoebozoa.fa'
# orgn='eukprot_amoebozoa'

for db in /mnt/mokosz/home/kika/allDB/renamed/*.faa ; do
	echo $db
	for profile in *.hmm ; do
		echo $profile
		folder='${profile%.hmm}'
		mkdir $folder
		cd hmmsearch/folder
		output=${db%.faa}'.'${profile%.hmm}.hmmsearch.table
		threads=10
		hmmsearch --tblout $output --cpu $threads $profile $db
		cd ../..
	done
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py HMMsearch done
