#!/bin/bash

datadir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Tetrapyrroles/precorrin-2_dehydrogenase/'
files=$datadir'*.fna'

for file in $files; do
	echo $file
	# makeblastdb -in $file -dbtype nucl -parse_seqids
	echo $file': BLASTable database done'
done
