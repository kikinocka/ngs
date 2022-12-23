#!/bin/bash

tRNAscan='/Users/kika/miniconda3/bin/tRNAscan-SE'

cd '/Users/kika/ownCloud/blastocrithidia/genome_assembly/'

for genome in p57_polished.fa ; do
	echo $genome

	table=${genome%.fa}.tRNAscan_table.tsv
	seq=${genome%.fa}.tRNAscan.fa
	structures=${genome%.fa}.tRNAscan_structures.txt

	$tRNAscan --thread 7 -o $table -a $seq -f $structures ${genome}
done
