#!/bin/bash

cd '/mnt/mokosz/home/kika/workdir/forn-bask/'
threads=15
eval=1e-05

#one profile and one database
db='Trepomonas_spPC1.faa'
profile='noTPC1_CLC.hmm'
out=${db%.faa}'.'${profile%.hmm}.hmmsearch.tsv
hmmsearch --tblout $out --cpu $threads -E $eval $profile $db


# #several profiles and one database
# db='/mnt/mokosz/home/kika/allDB/all.faa'
# orgn='all'

# for profile in *.hmm ; do
# 	out=$orgn'_'${profile%.hmm}.hmmsearch.tsv
# 	hmmsearch --tblout $out --cpu $threads -E $eval $profile $db
# done


# #one profile and several databases
# profile='noGiar_CLC.hmm'

# for db in Giardia*.faa ; do
# 	orgn=${db%.faa}
# 	out=${db%.faa}'.'${profile%.hmm}.hmmsearch.tsv
# 	hmmsearch --tblout $out --cpu $threads -E $eval $profile $db
# done
# # --max	Turn all heuristic filters off (less speed, more power) 


# #several profiles and several databases
# for profile in /mnt/mokosz/home/kika/metamonads/MRO_proteins/3-MRO+HMMhits_mafft+hmm/*.hmm ; do
# 	echo $profile
# 	folder=`echo $profile | cut -d / -f 9`
# 	folder=${folder%.mro+hmm.hmm}
# 	echo $folder
# 	for db in /mnt/mokosz/home/kika/allDB/renamed/*.faa ; do
# 		echo $db
# 		mkdir /mnt/mokosz/home/kika/metamonads/MRO_proteins/3-MRO+HMMhits_hmmsearch_eval-1e-05/$folder
# 		cd /mnt/mokosz/home/kika/metamonads/MRO_proteins/3-MRO+HMMhits_hmmsearch_eval-1e-05/$folder
# 		output=`echo $db | cut -d / -f 8`
# 		output=${output%.faa}
# 		# echo $output
# 		output=$output'.'${folder}.hmmsearch.tsv
# 		echo $output
# 		# output=${db%.faa}'.'${profile%.hmm}.hmmsearch.tsv
# 		# output=$orgn'_'${profile%.hmm}.hmmsearch.tsv
# 		hmmsearch --tblout $output --cpu $threads -E $eval $profile $db
# 		cd /mnt/mokosz/home/kika/metamonads/MRO_proteins/3-MRO+HMMhits_mafft+hmm/
# 		# sleep 5
# 		echo
# 	done
# done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py HMMsearch done
