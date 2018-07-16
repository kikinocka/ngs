#!/bin/bash

#where “NR%2==1” means that every 2nd line is modified (i.e., only the header of sequence and the header of quality 
#(but not the quality line itself)) by replacing underscore by a space “gsub(/_/," ")”

read_dir='/media/4TB1/diplonema/reads/transcriptome/trimmed/'
fwd_in=$read_dir'1604_trimmed_1.fq.gz'
rev_in=$read_dir'1604_trimmed_2.fq.gz'
fwd_out=$read_dir'1604_trimmed_1_se.fq.gz'
rev_out=$read_dir'1604_trimmed_2_se.fq.gz'

zcat $fwd_in | awk '{if(NR%2==1){gsub(/_/," ")}; print}' | gzip -c > $fwd_out
zcat $rev_in | awk '{if(NR%2==1){gsub(/_/," ")}; print}' | gzip -c > $rev_out
