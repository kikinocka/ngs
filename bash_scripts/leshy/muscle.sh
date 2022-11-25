#!/bin/sh

cd '/mnt/mokosz/home/kika/archam_trees/nadA'

for fasta in *.fa; do
	aln=${fasta%.fa}.muscle.aln
	log=${fasta%.fa}.muscle.log
	muscle -align $fasta -output $aln 2> $log
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py muscle5 done
