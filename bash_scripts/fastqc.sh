#!/bin/sh

read_dir='/home/kika/diplonema/reads/trimmed/'
out_dir='/home/kika/diplonema/reads/trimmed/fastqc/'

# /home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1604_adapter_trimmed_merged.fq'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1604_trimmed_1.fq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'YPF1604_trimmed_2.fq.gz'