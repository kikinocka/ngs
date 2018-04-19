#!/bin/bash

read_dir='/home/kika/diplonema/reads/transcriptome/raw/'
fw=$read_dir'HI.4229.008.Index_20.1621_R1.fastq.gz'
rv=$read_dir'HI.4229.008.Index_20.1621_R2.fastq.gz'
trimdir='/home/kika/diplonema/reads/transcriptome/trimmed/'
name='1621'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=r trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=30


read_dir='/home/kika/diplonema/reads/transcriptome/raw/'
fw=$read_dir'HI.4229.008.Index_25.1608a_R1.fastq.gz'
rv=$read_dir'HI.4229.008.Index_25.1608a_R2.fastq.gz'
trimdir='/home/kika/diplonema/reads/transcriptome/trimmed/'
name='1608'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=r trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=30


read_dir='/home/kika/diplonema/reads/transcriptome/raw/'
fw=$read_dir'HI.4229.008.Index_22.1618_R1.fastq.gz'
rv=$read_dir'HI.4229.008.Index_22.1618_R2.fastq.gz'
trimdir='/home/kika/diplonema/reads/transcriptome/trimmed/'
name='1618'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=r trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=30
