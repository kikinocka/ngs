#!/bin/bash

bw2_dir='/home/kika/miniconda3/pkgs/bowtie2-2.3.4.2-py36h2d50403_0/bin/'
base_name='/media/4TB1/diplonema/mapping/DNA_to_contigs/1610/1610_D03_bw2'
ref='/media/4TB1/diplonema/mapping/DNA_to_contigs/1610/1610_D03.fasta'

$bw2_dir'bowtie2-build' --threads 32 $ref $base_name

read_dir='/media/4TB1/diplonema/reads/genome/used/1610/'
p1_1=$read_dir'1610_D03_merged_deduplicated.fq'
p1_2=$read_dir'1610_D03_unmerged_deduplicated.fq'

samfile=$base_name'.sam'
report=$base_name'_report.txt'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq'
unmapped_paired=$base_name'_unmapped_paired.fq'

bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

$bw2_dir'bowtie2' --very-fast-local -p 32 -I 0 -X 5 -x $base_name \
-U $p1_1,$p1_2 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $samfile 2> $report

samtools view -bS $samfile > $bamfile -@ 32
samtools sort -o $sorted -@ 32 $bamfile
samtools index -b $sorted
