#!/bin/bash

read_dir='/home/kika/diplonema/reads/transcriptome/raw/'
fw=$read_dir'HI.4413.001.Index_21.1601b_R1.fastq.gz'
rv=$read_dir'HI.4413.001.Index_21.1601b_R2.fastq.gz'
trimdir='/home/kika/diplonema/reads/transcriptome/trimmed/'
name='1601'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=r trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=30


read_dir='/home/kika/diplonema/reads/transcriptome/raw/'
fw=$read_dir'HI.4413.001.Index_23.1604b_R1.fastq.gz'
rv=$read_dir'HI.4413.001.Index_23.1604b_R2.fastq.gz'
trimdir='/home/kika/diplonema/reads/transcriptome/trimmed/'
name='1604'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=r trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=30


read_dir='/home/kika/diplonema/reads/transcriptome/raw/'
fw=$read_dir'HI.4413.001.Index_9.1610_R1.fastq.gz'
rv=$read_dir'HI.4413.001.Index_9.1610_R2.fastq.gz'
trimdir='/home/kika/diplonema/reads/transcriptome/trimmed/'
name='1610'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=r trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=30
