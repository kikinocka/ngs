#!/bin/sh

cd '/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_fasta/'

for fasta in *.fa; do
	echo $fasta
	aln=${fasta%.fa}.muscle.aln
	log=${fasta%.fa}.muscle.log

	# #short alns
	# muscle -threads 10 -align $fasta -output $aln 2> $log
	
	#long alns
	muscle -threads 15 -super5 $fasta -output $aln 2> $log
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py muscle5 done
