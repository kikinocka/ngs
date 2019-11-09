#!/bin/sh

read_dir='/home/kika/work_dir/'
out_dir='/home/kika/work_dir/fastqc/'

/home/kika/tools/FastQC/fastqc -t 30 -o $out_dir $read_dir'SRR2048652_1.fastq.gz'
/home/kika/tools/FastQC/fastqc -t 30 -o $out_dir $read_dir'SRR2048652_2.fastq.gz'
/home/kika/tools/FastQC/fastqc -t 30 -o $out_dir $read_dir'SRR2048652_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -t 30 -o $out_dir $read_dir'SRR2048652_trimmed_2.fq.gz'
