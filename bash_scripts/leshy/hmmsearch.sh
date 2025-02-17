#!/bin/bash

cd '/mnt/mokosz/home/kika/metamonads/MRO_proteins/metamonads_assemblies/'
threads=15
eval=1e-10

# #several profiles and one database
# db='/mnt/mokosz/home/kika/allDB/renamed/all.fa'
# orgn='all'

# for profile in *.hmm ; do
# 	out=$orgn'_'${profile%.hmm}.hmmsearch.tsv
# 	hmmsearch --tblout $out --cpu $threads -E $eval $profile $db
# done

# #one profile and several database
# workdir='/mnt/mokosz/home/kika/workdir/'
# profile=$workdir'archaea_eRF1.hmm'

# for db in *.faa ; do
# 	orgn=${db%.faa}
# 	out=$orgn'.eRF1_hmmsearch.tsv'
# 	hmmsearch --tblout $out --cpu $threads -E $eval $profile $db
# done

# mv *tsv $workdir

#several profiles and several databases
for profile in /mnt/mokosz/home/kika/metamonads/MRO_proteins/MRO_hmm/*.hmm ; do
	echo $profile
	folder=`echo $profile | cut -d / -f 9`
	folder=${folder%.hmm}
	echo $folder
	
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py HMMsearch done
