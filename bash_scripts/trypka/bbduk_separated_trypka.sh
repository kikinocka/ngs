#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/reads/tRNAs/'
fw=$read_dir'p57_tRNA_1.fastq.gz'
rv=$read_dir'p57_tRNA_2.fastq.gz'
trimdir='/media/4TB1/blastocrithidia/reads/tRNAs/'
name='p57_tRNA'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=30
