#!/bin/bash

cd '/mnt/mokosz/home/kika/rhizomastix_vacuolata/mapping/rvac1/'
assembly_dir='/mnt/mokosz/home/kika/rhizomastix_vacuolata/rvac_NR/'
read_dir='/mnt/mokosz/home/kika/rhizomastix_vacuolata/reads/'

base_name='rvac1_bw2'
ref=$assembly_dir'rvac.trinity.NRfilt.fna'
p1_1=$read_dir'RV1_trimmed_1.fq.gz'
p1_2=$read_dir'RV1_trimmed_2.fq.gz'
cpu=10

samfile=$base_name'.sam'
report=$base_name'.report.txt'
bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

bowtie2-build --threads $cpu $ref $base_name
bowtie2 --very-sensitive -p $cpu \
	-x $base_name \
	-1 $p1_1 \
	-2 $p1_2 \
	--no-unal \
	-S $samfile 2> $report

samtools view -bS $samfile > $bamfile -@ $cpu 
samtools sort -o $sorted -@ $cpu $bamfile 
samtools index $sorted
