#!/bin/bash

bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
read_dir='/home/kika/diplonema/reads/transcriptome/raw/'
base_name='/home/kika/diplonema/transcripts/1601/1601_bw2'
ref='/home/kika/diplonema/transcripts/1601/1601_candidates_nt.fasta'
$bw2_dir'bowtie2-build' --threads 32 $ref $base_name

p1_1=$read_dir'HI.4413.001.Index_21.1601b_R1.fastq.gz'
p1_2=$read_dir'HI.4413.001.Index_21.1601b_R2.fastq.gz'

alignment=$base_name".sam"
report=$base_name".txt"
unmapped_unpaired=$base_name"_unmapped_unpaired.fq"
unmapped_paired=$base_name"_unmapped_paired.fq"

$bw2_dir'bowtie2' --very-sensitive -p 32 -x $base_name -1 $p1_1 -2 $p1_2 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $alignment 2> $report

samfile=$alignment
bamfile=$base_name"_unsorted.bam"
sorted=$base_name"_sorted"
sorted_file=$sorted".bam"

samtools view -bS $samfile > $bamfile -@ 32
samtools sort -o $sorted_file -@ 32 $bamfile
samtools index -b $sorted_file