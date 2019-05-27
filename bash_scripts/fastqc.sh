#!/bin/sh

read_dir='/media/4TB1/blastocrithidia/reads/tRNAs/'
out_dir='/media/4TB1/blastocrithidia/reads/tRNAs/fastqc/'

/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'p57_tRNA_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'p57_tRNA_trimmed_2.fq.gz'
