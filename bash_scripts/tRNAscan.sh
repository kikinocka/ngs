#!/bin/bash

tRNAscan='/Users/kika/miniconda3/bin/tRNAscan-SE'

cd '/Users/kika/data/opisthokonta/'

for genome in *genomic.fna ; do
	echo $genome

	table=${genome%.fna}.tRNAscan_table.tsv
	seq=${genome%.fna}.tRNAscan.fa
	structures=${genome%.fna}.tRNAscan_structures.txt

	$tRNAscan --thread 6 -o $table -a $seq -f $structures ${genome}
done
