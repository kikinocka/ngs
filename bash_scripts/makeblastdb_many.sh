#!/bin/bash

cd '/mnt/mokosz/home/zoli/proj/Euglena_v2/databases/'

for file in *.fasta; do
	echo $file
	makeblastdb -in $file -dbtype nucl -parse_seqids
	echo $file': BLASTable database done'
done
