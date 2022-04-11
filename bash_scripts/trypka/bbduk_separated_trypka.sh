#!/bin/bash

bbduk='/home/kika/tools/bbmap/bbduk.sh'
threads=40

read_dir='/media/4TB1/blastocrithidia/reads/transcriptome/raw/'
fw=$read_dir'Blastoc_spP57_1.fastq.gz'
rv=$read_dir'Blastoc_spP57_2.fastq.gz'
trimdir='/media/4TB1/blastocrithidia/new_3-UTR/'
name='p57'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

# $bbduk overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=$threads
$bbduk in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapters usejni=t ktrim=r k=22 mink=11 hdist=2 tpe t=$threads 2> $report
