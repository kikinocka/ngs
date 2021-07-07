#!/bin/bash

cd '/mnt/mokosz/home/kika/rhizomastix_libera+elongata_reassembly/mapping/'
assembly_dir='/mnt/mokosz/home/kika/rhizomastix_libera+elongata_reassembly/rhizomastix_reassembly_NR/'
read_dir='/mnt/mokosz/home/kika/rhizomastix_libera+elongata_reassembly/reads/'

base_name='rvac2_bw2'
ref=$assembly_dir'rhizomastix_reassembly.trinity.NRfilt.fasta'
p1_1=$read_dir'SRR5396411_trimmed_1.fq.gz'
p1_2=$read_dir'SRR5396411_trimmed_2.fq.gz'
p2_1=$read_dir'SRR5396412_trimmed_1.fq.gz'
p2_2=$read_dir'SRR5396412_trimmed_2.fq.gz'
cpu=10

samfile=$base_name'.sam'
report=$base_name'.report.txt'
bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

bowtie2-build --threads $cpu $ref $base_name
bowtie2 --very-sensitive -p $cpu \
	-x $base_name \
	-1 $p1_1,$p2_1 \
	-2 $p1_2,$p2_2 \
	--no-unal \
	-S $samfile 2> $report

samtools view -bS $samfile > $bamfile -@ $cpu 
samtools sort -o $sorted -@ $cpu $bamfile 
samtools index $sorted
