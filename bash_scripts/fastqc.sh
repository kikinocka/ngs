#!/bin/sh

read_dir='/home/kika/diplonema/reads/trimmed/'
out_dir='/home/kika/diplonema/reads/trimmed/fastqc/'

/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1610_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1610_trimmed_2.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1601_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1601_trimmed_2.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1604_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1604_trimmed_2.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1618_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1618_trimmed_2.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1621_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1621_trimmed_2.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1608_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1608_trimmed_2.fq.gz'