#!/bin/bash

filt_script='/Users/kika/scripts/py_scripts/filter_alignment.py'

cd '/Users/kika/ownCloud/diplonema/pyruvate_metabolism/PDH/aceE/ver6/'
fasta='aceE.trimal_gt-0.8.aln'
threshold=50

$filt_script -f $fasta -t $threshold
