#!/bin/bash

replacer='/Users/kika/ownCloud/lab_documents/Joel/lael_scripts/name_replace/name_replace.pl'

# cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_COPII/trees/hyp27/ver2/'
cd '/Users/kika/ownCloud/archamoebae/trees/rho/ver7_muscle/'

for aln in *.mafft.aln ; do
	out=${aln%.mafft.aln}.CD.mafft.aln
	table=${aln%.mafft.aln}.table
	perl $replacer -f $aln $out $table
done
