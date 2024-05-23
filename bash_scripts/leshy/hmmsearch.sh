#!/bin/bash

cd '/mnt/mokosz/home/kika/allDB/renamed/'
threads=15
eval=1e-10

# #several profiles and one database
# db='/mnt/mokosz/home/kika/allDB/renamed/all.fa'
# orgn='all'

# for profile in *.hmm ; do
# 	out=$orgn'_'${profile%.hmm}.hmmsearch.tsv
# 	hmmsearch --tblout $out --cpu $threads -E $eval $profile $db
# done

#one profile and several database
workdir='/mnt/mokosz/home/kika/workdir/'
profile=$workdir'archaea_eRF1.hmm'

for db in *.faa ; do
	orgn=${db%.faa}
	out=$orgn'_'${profile%.hmm}.hmmsearch.tsv
	hmmsearch --tblout $out --cpu $threads -E $eval $profile $db
done

mv *tsv $workdir

# #several profiles and several databases
# for profile in /mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/*.hmm ; do
# 	echo $profile
# 	folder=`echo $profile | cut -d / -f 8`
# 	folder=${folder%.hmm}
# 	# echo $folder
# 	for db in /mnt/mokosz/home/kika/allDB/renamed/*.fa ; do
# 		echo $db
# 		# mkdir /mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/hmmsearch/$folder
# 		cd /mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/hmmsearch/$folder
# 		output=`echo $db | cut -d / -f 8`
# 		output=${output%.fa}
# 		# echo $output
# 		output=$output'.'${folder}.hmmsearch.tsv
# 		# echo $output
# 		# output=${db%.faa}'.'${profile%.hmm}.hmmsearch.tsv
# 		# output=$orgn'_'${profile%.hmm}.hmmsearch.tsv
# 		hmmsearch --tblout $output --cpu $threads -E $eval $profile $db
# 		# cd /mnt/mokosz/home/kika/metamonads_ancestral/OGs_hmm/
# 		# sleep 5
# 		echo
# 	done
# done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py HMMsearch done
