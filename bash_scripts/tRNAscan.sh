#!/bin/bash

tRNAscan='/Users/kika/miniconda3/bin/tRNAscan-SE'

cd '/Users/kika/ownCloud/blasto_comparative/genomes/'

# for assembly in atp6_contigs.fa ; do
# 	echo $assembly
# 	table=${assembly%.fasta}.tRNAscan_table.out
# 	seq=${assembly%.fasta}.tRNAscan.fa
# 	structures=${assembly%.fasta}.tRNAscan_structures.out
# 	$tRNAscan --thread 5 -o $table -a $seq -f $structures ${assembly}
# done


for genome in *_masked.fa ; do
	echo $genome

	table=${genome%.fa}.tRNAscan_table.tsv
	seq=${genome%.fa}.tRNAscan.fa
	structures=${genome%.fa}.tRNAscan_structures.txt

	$tRNAscan --thread 7 -o $table -a $seq -f $structures ${genome}

done
