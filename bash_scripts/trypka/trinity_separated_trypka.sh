#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/new_3-UTR/trimmed_RNA_reads/'
fw=$read_dir'p57_trimmed_1.fq.gz',$read_dir'p57_3-end_trimmed_1.fq.gz'
rv=$read_dir'p57_trimmed_2.fq.gz',$read_dir'p57_3-end_trimmed_2.fq.gz'
out_dir='/media/4TB1/blastocrithidia/new_3-UTR/p57_trinity_all/'

Trinity --seqType fq --left $fw --right $rv --output $out_dir --max_memory 100G --CPU 30

