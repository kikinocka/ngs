#!/bin/bash

cd '/mnt/mokosz/home/kika/metamonads/MRO_proteins/3-MRO+HMMhits_fasta/again/'

threads=10

for msa in *.aln ; do
	echo $msa
	name=${msa%mafft.aln}
	hmm=${msa%.mafft.aln}.hmm
	summary=${msa%.mafft.aln}.hmmbuild.log
	hmmbuild -n $name -o $summary --amino --cpu $threads $hmm $msa
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py HMMbuild done
