#!/bin/bash

bbduk='/home/kika/tools/bbmap/bbduk.sh'
threads=30

read_dir='/media/4TB1/blastocrithidia/reads/transcriptome/raw/'
fw=$read_dir'p57_3-end_enriched_1.fastq.gz'
rv=$read_dir'p57_3-end_enriched_2.fastq.gz'
trimdir='/media/4TB1/blastocrithidia/new_3-UTR/20220603_trimmed_RNA_reads_mink5/'
name='p57_3-end'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_bbduk_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

# $bbduk in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=11 mink=11 hdist=2 tpe t=$threads 2> $report
$bbduk in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t ktrim=r k=22 mink=5 hdist=2 tpe t=$threads 2> $report
