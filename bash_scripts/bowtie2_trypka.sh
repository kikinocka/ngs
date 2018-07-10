#!/bin/bash

bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
base_name='/media/4TB1/diplonema/mapping/DNA_to_contigs/1618/1618_DNA_bw2'
ref='/media/4TB1/diplonema/mapping/DNA_to_contigs/1618/1618_DNA_contigs.fasta'
$bw2_dir'bowtie2-build' --threads 32 $ref $base_name

read_dir='/media/4TB1/diplonema/reads/genome/merged/'
p1_1=$read_dir'YPF1618_merged_deduplicated.fq'
# p1_2=$read_dir'YPF1601_trimmed_2.fq.gz'

alignment=$base_name'.sam'
report=$base_name'_report.txt'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq'
unmapped_paired=$base_name'_unmapped_paired.fq'

$bw2_dir'bowtie2' --very-sensitive -p 32 -x $base_name -U $p1_1 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $alignment 2> $report
#-1 $p1_1 -2 $p1_2 

samfile=$alignment
bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted'
sorted_file=$sorted'.bam'

samtools view -bS $samfile > $bamfile -@ 32
samtools sort -o $sorted_file -@ 32 $bamfile
samtools index -b $sorted_file