#!/bin/bash

read_dir='/home/kika/diplonema/reads/raw/'
fw=$read_dir'MI.M03555_0253.001.Index_2.YPF1601_R1.fastq.gz'
rv=$read_dir'MI.M03555_0253.001.Index_2.YPF1601_R2.fastq.gz'
trimdir='/home/kika/diplonema/reads/trimmed/'
name='YPF1601'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=r trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=30


read_dir='/home/kika/diplonema/reads/raw/'
fw=$read_dir'MI.M03555_0253.001.Index_18.YPF1610b_R1.fastq.gz'
rv=$read_dir'MI.M03555_0253.001.Index_18.YPF1610b_R2.fastq.gz'
trimdir='/home/kika/diplonema/reads/trimmed/'
name='1610'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=r trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=30


read_dir='/home/kika/diplonema/reads/raw/'
fw=$read_dir'MI.M03555_0253.001.Index_7.1621b_R1.fastq.gz'
rv=$read_dir'MI.M03555_0253.001.Index_7.1621b_R2.fastq.gz'
trimdir='/home/kika/diplonema/reads/trimmed/'
name='YPF1621'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=r trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=30


read_dir='/home/kika/diplonema/reads/raw/'
fw=$read_dir'MI.M03555_0253.001.Index_6.YPF1608_R1.fastq.gz'
rv=$read_dir'MI.M03555_0253.001.Index_6.YPF1608_R2.fastq.gz'
trimdir='/home/kika/diplonema/reads/trimmed/'
name='YPF1608'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=r trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=30
