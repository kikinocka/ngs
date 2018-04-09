#!/bin/sh

read_dir='/home/kika/diplonema/reads/transcriptome/trimmed/'
out_dir='/home/kika/diplonema/reads/transcriptome/trimmed/fastqc/'

/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'1601_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'1601_trimmed_2.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'1604_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'1604_trimmed_2.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'1610_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'1610_trimmed_2.fq.gz'
