#!/bin/sh

#align denovo
cd '/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_muscle/'

for a in *.muscle.aln ; do
	echo $f
	out=${f%.muscle.aln}.trimal_gt-0.8.aln
	trimal -in $f -out $out -gt 0.8 -fasta
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py trimAl done
