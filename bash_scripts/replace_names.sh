#!/bin/bash

replacer='/Users/kika/ownCloud/lab_documents/Joel/lael_scripts/name_replace/name_replace.pl'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/ARFs/ph-arf/ver4/'

for aln in *0.8.aln ; do
	out=${aln%.trimal_gt-0.8.aln}.CD.trimal_gt-0.8.aln
	table=${aln%.aln}.table
	perl $replacer -f $aln $out $table
done
