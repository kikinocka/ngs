#!/bin/bash

# bw2_dir='/home/kika/miniconda3/pkgs/bowtie2-2.3.4.2-py36h2d50403_0/bin/'
ref='/media/4TB1/blastocrithidia/new_3-UTR/p57_trinity_all/Trinity.fasta'

read_dir='/media/4TB1/blastocrithidia/new_3-UTR/trimmed_RNA_reads/'
p1_1=$read_dir'p57_all_trimmed_1.fq.gz'
p1_2=$read_dir'p57_all_trimmed_2.fq.gz'


cd '/media/4TB1/blastocrithidia/new_3-UTR/bw2_mapping_transcriptome/p57_all/'
base_name='p57_all'
samfile=$base_name'.sam'
report=$base_name'_report.txt'
# unmapped_unpaired=$base_name'_unmapped_unpaired.fq'
# unmapped_paired=$base_name'_unmapped_paired.fq'
unsorted=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'


bowtie2-build --threads 30 $ref $base_name

# bowtie2 --very-sensitive -p 30 -x $base_name \
# 	-1 $p1_1 -2 $p1_2 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $samfile 2> $report

bowtie2 --very-sensitive -p 30 -x $base_name \
	-1 $p1_1 -2 $p1_2 -S $samfile 2> $report

# bowtie2 --very-sensitive -p 30 -x $base_name \
# 	-U $p1_2 -S $samfile 2> $report

samtools view -bS -@ 30 $samfile > $unsorted
samtools sort -o $sorted -@ 30 $unsorted
samtools index -b $sorted
