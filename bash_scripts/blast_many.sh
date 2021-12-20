#!/bin/bash

datadir='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Tetrapyrroles/precorrin-2_dehydrogenase/'
program=tblastn
query=$datadir'query.fa'
outfmt=7
word=3
files=$datadir'*.fna'

for db in $files; do
	echo $db
	out=${db%.*}'.tblastn.out'
	$program -query $query -db $db -out $out -outfmt $outfmt -word_size $word -num_threads 4
	echo ***BLAST done***
done
