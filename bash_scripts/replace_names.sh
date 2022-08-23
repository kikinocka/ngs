#!/bin/bash

replacer='/Users/kika/ownCloud/lab_documents/Joel/lael_scripts/name_replace/name_replace.pl'

# cd '/Users/kika/ownCloud/membrane-trafficking/sec13-MS/wdr/tree/ver9/'
cd '/Users/kika/ownCloud/archamoebae/trees/PFO/ver4/MrBayes/'

for aln in *.mafft.aln ; do
	out=${aln%.mafft.aln}.CD.mafft.aln
	table=${aln%.mafft.aln}.table
	perl $replacer -f $aln $out $table
done
