#!/bin/bash

cd '/media/4TB1/blastocrithidia/new_3-UTR/20220523_trimmed_RNA_reads/'
fastqc='/home/nenarokova/tools/FastQC/fastqc'

outdir='/media/4TB1/blastocrithidia/new_3-UTR/20220523_trimmed_RNA_reads/fastqc/'

for file in *.gz; do
	echo $file
	fastqc -o $SCRATCHDIR $file
done
