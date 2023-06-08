#!/bin/sh

cd '/mnt/mokosz/home/kika/workdir'

for fasta in *.fa; do
	aln=${fasta%.fa}.muscle_super5.aln
	log=${fasta%.fa}.muscle_super5.log
	muscle -super5 $fasta -output $aln 2> $log
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py muscle5-super5 done
