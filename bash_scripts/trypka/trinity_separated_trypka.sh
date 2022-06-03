#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/new_3-UTR/20220603_trimmed_RNA_reads_mink5/'
fw=$read_dir'p57_trimmed_1.fq.gz',$read_dir'p57_3-end_trimmed_1.fq.gz'
rv=$read_dir'p57_trimmed_2.fq.gz',$read_dir'p57_3-end_trimmed_2.fq.gz'
out_dir='/media/4TB1/blastocrithidia/new_3-UTR/20220603_trinity/'

Trinity --seqType fq --left $fw --right $rv --output $out_dir --max_memory 100G --CPU 30
