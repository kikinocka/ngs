#!/bin/bash

cd '/mnt/data/kika/references/'

for file in *.fasta; do
	echo $file
	makeblastdb -in $file -dbtype prot -parse_seqids
	echo $file': BLASTable database done'
done
