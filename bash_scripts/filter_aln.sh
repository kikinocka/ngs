#!/bin/bash

filt_script='/Users/kika/scripts/py_scripts/filter_alignment.py'

cd '/Users/kika/ownCloud/diplonema/pyruvate_metabolism/PDH/E1b/ver6/'
threshold=50

for fasta in *trimal*.aln ; do
	$filt_script -f $fasta -t $threshold
done