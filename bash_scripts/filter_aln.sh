#!/bin/bash

filt_script='/mnt/mokosz/home/kika/scripts/py_scripts/filter_alignment.py'

cd '/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_trimal_automated1/'
threshold=50

for fasta in *trimal*.aln ; do
	$filt_script -f $fasta -t $threshold
done
