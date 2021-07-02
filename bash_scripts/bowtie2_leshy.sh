#!/bin/bash

cd '/mnt/mokosz/home/kika/endolimax_nana/mapping/endo1/'
assembly_dir='/mnt/mokosz/home/kika/endolimax_nana/enan_NR/'
read_dir='/mnt/mokosz/home/kika/endolimax_nana/reads//'

base_name='endo1_bw2'
ref=$assembly_dir'enan.trinity.NRfilt.faa'
p1_1=$assembly_dir'Endo1_trimmed_1.fq.gz'
p1_2=$assembly_dir'Endo1_trimmed_2.fq.gz'
cpu=10

samfile=$base_name'.sam'
mapped=$base_name'_mapped.fq.gz'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq.gz'
unmapped_paired=$base_name'_unmapped_paired.fq.gz'
report=$base_name'.report.txt'
bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

bowtie2-build --threads $cpu $ref $base_name
bowtie2 --very-sensitive -p $cpu \
	-x $base_name \
	-1 $p1_1 \
	-2 $p1_2 \
	--no-unal \
	--un-gz $unmapped_unpaired \
	--un-conc-gz $unmapped_paired \
	--al-conc-gz $mapped \
	-S $samfile 2> $report
	# -U $r1,$r2 \

samtools view -bS $samfile > $bamfile -@ $cpu 
samtools sort -o $sorted -@ $cpu $bamfile 
samtools index $sorted
