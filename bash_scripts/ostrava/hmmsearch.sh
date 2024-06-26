#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N hmmsearch
#PBS -l nodes=1:ppn=15
#PBS -l walltime=100:00:00

cd '/home/users/kika/schizosaccharomyces_japonicus/hmms/'
threads=15
evalue=1e-05

#several profiles and one database
db='/home/users/kika/schizosaccharomyces_japonicus/control/ovol_translated.fa'
orgn='ovol'

for profile in *.hmm ; do
	out=$orgn'_'${profile%.trimal_gt-0.8.aln.hmm}.hmmsearch.tsv
	hmmsearch --tblout $out --cpu $threads -E $evalue $profile $db
done


python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: hmmsearch done
