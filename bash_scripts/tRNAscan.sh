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


assembly='triat_scaffolds.fasta'
table=${assembly%.fasta}.tRNAscan_table.out
seq=${assembly%.fasta}.tRNAscan.fa
structures=${assembly%.fasta}.tRNAscan_structures.out

$tRNAscan --thread 5 -o $table -a $seq -f $structures ${assembly}
