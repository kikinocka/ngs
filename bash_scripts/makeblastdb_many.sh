#!/bin/bash

cd '/mnt/mokosz/home/kika/eukprot_amoebozoa/'

for file in *.fa; do
	echo $file
	makeblastdb -in $file -dbtype prot -parse_seqids
	echo $file': BLASTable database done'
done
