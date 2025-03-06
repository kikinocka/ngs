#!/bin/bash

filt_script='/mnt/mokosz/home/kika/scripts/py_scripts/filter_alignment.py'

cd '/mnt/mokosz/home/kika/metamonads/MRO_proteins/3-MRO+HMMhits_trimal_gt-0.8/'
threshold=50

for fasta in *trimal*.aln ; do
	echo $fasta
	$filt_script -f $fasta -t $threshold
done
