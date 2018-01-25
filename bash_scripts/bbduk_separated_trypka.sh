#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=60

read_dir='/home/kika/diplonema/reads/raw/'
fw=$read_dir'MI.M03555_0253.001.Index_13.YPF1604_R1.fastq.gz'
rv=$read_dir'MI.M03555_0253.001.Index_13.YPF1604_R2.fastq.gz'
trimdir='/home/kika/diplonema/reads/trimmed/'
name='YPF1604'
trimmed_fw=$trimdir$name'_trimmed_1.fq.gz'
trimmed_rv=$trimdir$name'_trimmed_2.fq.gz'
report=$trimdir$name"_report.txt"
adapt='/home/kika/tools/bbmap/resources/adapters.fa'

/home/kika/tools/bbmap/bbduk.sh overwrite=true in1=$fw in2=$rv out1=$trimmed_fw out2=$trimmed_rv ref=$adapt usejni=t qtrim=r trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=30
# 