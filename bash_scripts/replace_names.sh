#!/bin/bash

replacer='/Users/kika/ownCloud/lab_documents/Joel/lael_scripts/name_replace_lael/name_replace.pl'

cd '/Users/kika/ownCloud/membrane-trafficking/trees/ArfGAPs/ag-smap-acap/ver4/'

for aln in *aln ; do
	out=${aln%.mafft.aln}.coded.mafft.aln
	table=${aln%.mafft.aln}.table
	perl $replacer -f $aln $out $table
done
