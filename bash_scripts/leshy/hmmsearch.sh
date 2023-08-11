#!/bin/bash

cd '/mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/'

db='/mnt/mokosz/home/kika/eukprot_amoebozoa/amoebozoa.fa'
# orgn='eukprot_amoebozoa'
threads=10

for profile in /mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/*.hmm ; do
	echo $profile
	folder=`echo $profile | cut -d / -f 8`
	folder=${folder%.hmm}
	# echo $folder
	for  db in /mnt/mokosz/home/kika/allDB/renamed/*.faa; do
		echo $db
		mkdir /mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/hmmsearch/$folder
		cd /mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/hmmsearch/$folder
		output=`echo $db | cut -d / -f 8`
		output=${output%.faa}
		# echo $output
		output=$output'.'${folder}.hmmsearch.tsv
		# echo $output
		# output=${db%.faa}'.'${profile%.hmm}.hmmsearch.tsv
		# output=$orgn'_'${profile%.hmm}.hmmsearch.tsv
		hmmsearch --tblout $output --cpu $threads $profile $db
		# cd /mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/
		sleep 5
		echo
	done
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py HMMsearch done
