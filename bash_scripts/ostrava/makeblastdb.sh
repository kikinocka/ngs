#!/bin/bash

cd '/mnt/data/kika/kineto_refs/'

for file in *.fa; do
	echo $file
	makeblastdb -in $file -dbtype prot -parse_seqids
	echo $file': BLASTable database done'
done
