#!/bin/bash

#align denovo
cd '/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_muscle/'

for f in *.muscle.aln ; do
	echo $f
	
	out=${f%.muscle.aln}.trimal_at1.aln
	trimal -in $f -out $out -automated1 -fasta
	
	out=${f%.muscle.aln}.trimal_gt-0.8.aln
	trimal -in $f -out $out -gt 0.8 -fasta

	# out=${f%.muscle.aln}.trimal_gt-0.8_cons-50.aln
	# trimal -in $f -out $out -gt 0.8 -cons 50 -fasta
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py trimAl done
