#!/bin/bash

cd '/mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/'

db='/mnt/mokosz/home/kika/eukprot_amoebozoa/amoebozoa.fa'
# orgn='eukprot_amoebozoa'

for db in /mnt/mokosz/home/kika/allDB/renamed/*.faa ; do
	echo $db
	for profile in /mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/*.hmm ; do
		echo $profile
		folder=$profile | cut -d / -f8
		folder=${profile%.hmm}
		echo $folder
		# mkdir /mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/hmmsearch/$folder
		# cd /mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/hmmsearch/$folder
		# output=$db | cut -d / -f8
		# output=$output'.'${profile%.hmm}.hmmsearch.tsv
		# echo $output
		#output=${db%.faa}'.'${profile%.hmm}.hmmsearch.tsv
		# output=$orgn'_'${profile%.hmm}.hmmsearch.tsv
		# threads=10
		# hmmsearch --tblout $output --cpu $threads $profile $db
		# cd /mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/
		sleep 5
	done
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py HMMsearch done
