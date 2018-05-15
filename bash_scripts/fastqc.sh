#!/bin/sh

read_dir='/media/4TB1/blastocrithidia/reads/transcriptome/trimmed/'
out_dir='/media/4TB1/blastocrithidia/reads/transcriptome/trimmed/fastqc/'

/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'p57_3-end_enriched_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'p57_3-end_enriched_trimmed_2.fq.gz'
