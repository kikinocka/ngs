#!/bin/bash

tRNAscan='/Users/kika/miniconda3/bin/tRNAscan-SE'

cd '/Users/kika/ownCloud/amoebophrya/'

for genome in *.fasta ; do
	echo $genome

	table=${genome%.fasta}.tRNAscan_table.tsv
	seq=${genome%.fasta}.tRNAscan.fa
	structures=${genome%.fasta}.tRNAscan_structures.txt

	$tRNAscan --thread 6 -o $table -a $seq -f $structures ${genome}
done
