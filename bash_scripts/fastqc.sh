#!/bin/sh

read_dir='/media/4TB1/blastocrithidia/reads/ku_mutants/'
out_dir='/media/4TB1/blastocrithidia/reads/ku_mutants//fastqc/'

/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'Lmex_Ku70_cl_9_1.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'Lmex_Ku70_cl_9_2.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'Lmex_Ku80_cl_2_1.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'Lmex_Ku80_cl_2_2.fastq.gz'
