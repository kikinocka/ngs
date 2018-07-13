#!/bin/bash

read_dir='/media/4TB1/diplonema/reads/transcriptome/trimmed/'
fwd_in=$read_dir'1604_trimmed_1.fq.gz'
rev_in=$read_dir'1604_trimmed_2.fq.gz'
fwd_out=$read_dir'1604_trimmed_1_se.fq.gz'
rev_out=$read_dir'1604_trimmed_2_se.fq.gz'

zcat $fwd_in | paste - - - - | awk 'BEGIN{FS="\t"; OFS="\n"}{sub("_", " ", $1); print}' | gzip -c > $fwd_out
zcat $rev_in | paste - - - - | awk 'BEGIN{FS="\t"; OFS="\n"}{sub("_", " ", $1); print}' | gzip -c > $rev_out
