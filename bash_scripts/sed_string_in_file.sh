#!/bin/bash

workdir='/Users/kika/ownCloud/membrane-trafficking/trees/COPII/'
files=$workdir'*trimal_gt_0.5.aln'

for file in $files; do
	echo $file
	out=${file%.*}'_new.trimal_gt_0.5.aln'
	cat $file | sed 's/Artemidia_lanifica/Artemidia_motanka/g' > $out
done
