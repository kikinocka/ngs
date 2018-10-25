#!/bin/sh

read_dir='/media/4TB1/diplonema/reads/transcriptome/raw/'
out_dir='/media/4TB1/diplonema/reads/transcriptome/raw/fastqc/'

/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'HI.4413.001.Index_21.1601b_R1.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'HI.4413.001.Index_21.1601b_R2.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'HI.4413.001.Index_23.1604b_R1.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'HI.4413.001.Index_23.1604b_R2.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'HI.4229.008.Index_25.1608a_R1.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'HI.4229.008.Index_25.1608a_R2.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'HI.4229.008.Index_22.1618_R1.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'HI.4229.008.Index_22.1618_R2.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'HI.4413.001.Index_9.1610_R1.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'HI.4413.001.Index_9.1610_R2.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'HI.4229.008.Index_20.1621_R1.fastq.gz'
/home/kika/tools/FastQC/fastqc -o $out_dir $read_dir'HI.4229.008.Index_20.1621_R2.fastq.gz'
