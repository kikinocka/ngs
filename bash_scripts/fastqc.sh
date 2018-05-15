#!/bin/sh

read_dir='/media/4TB1/blastocrithidia/reads/transcriptome/'
out_dir='/media/4TB1/blastocrithidia/reads/transcriptome/raw/fastqc/'

/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'raw/p57_3-end_enriched_1.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'raw/p57_3-end_enriched_2.fastq.gz'
