#!/bin/bash

replacer='/Users/kika/ownCloud/lab_documents/Joel/lael_scripts/name_replace/name_replace.pl'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_ESCRTs/ESCRT-0/tree/backbone/ver10/'

for aln in *0.8.aln ; do
	out=${aln%.trimal_gt-0.8.aln}.CD.trimal_gt-0.8.aln
	table=${aln%.trimal_gt-0.8.aln}.codes_names.txt
	perl $replacer -f $aln $out $table
done
