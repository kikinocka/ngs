#!/bin/bash

replacer='/Users/kika/ownCloud/lab_documents/Joel/lael_scripts/name_replace/name_replace.pl'

cd '/Users/kika/ownCloud/archamoebae/trees/AAT/ver6/'

for aln in *.aln ; do
	out=${aln%.aln}.CD.aln
	table=${aln%.aln}.table
	perl $replacer -f $aln $out $table
done
