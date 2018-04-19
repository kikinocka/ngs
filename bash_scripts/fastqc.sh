#!/bin/sh

read_dir='/home/kika/diplonema/reads/transcriptome/trimmed/'
out_dir='/home/kika/diplonema/reads/transcriptome/trimmed/fastqc/'

/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'1608_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'1608_trimmed_2.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'1618_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'1618_trimmed_2.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'1621_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'1621_trimmed_2.fq.gz'
