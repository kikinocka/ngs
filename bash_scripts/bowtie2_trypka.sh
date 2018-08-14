#!/bin/bash

bw2_dir='/home/kika/miniconda3/pkgs/bowtie2-2.3.4.2-py36h2d50403_0/bin/'
base_name='/media/4TB1/diplonema/mapping/RNA_to_transcriptomes/1601/1601_RNA_full_bw2'
ref='/media/4TB1/diplonema/transcriptomes/1601_Trinity.fasta'
$bw2_dir'bowtie2-build' --threads 32 $ref $base_name

read_dir='/media/4TB1/diplonema/reads/transcriptome/trimmed/'
p1_1=$read_dir'1601_trimmed_1.fq.gz'
p1_2=$read_dir'1601_trimmed_2.fq.gz'

alignment=$base_name'.sam'
report=$base_name'_report.txt'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq'
unmapped_paired=$base_name'_unmapped_paired.fq'

$bw2_dir'bowtie2' --very-sensitive -p 32 -x $base_name -1 $p1_1 -2 $p1_2 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $alignment 2> $report
#-U $p1_1 

# samfile=$alignment
# bamfile=$base_name'_unsorted.bam'
# sorted=$base_name'_sorted'
# sorted_file=$sorted'.bam'

# samtools view -bS $samfile > $bamfile -@ 32
# samtools sort -o $sorted_file -@ 32 $bamfile
# samtools index -b $sorted_file


bw2_dir='/home/kika/miniconda3/pkgs/bowtie2-2.3.4.2-py36h2d50403_0/bin/'
base_name='/media/4TB1/diplonema/mapping/RNA_to_transcriptomes/1618/1618_RNA_full_bw2'
ref='/media/4TB1/diplonema/transcriptomes/1618_Trinity.fasta'
$bw2_dir'bowtie2-build' --threads 32 $ref $base_name

read_dir='/media/4TB1/diplonema/reads/transcriptome/trimmed/'
p1_1=$read_dir'1618_trimmed_1.fq.gz'
p1_2=$read_dir'1618_trimmed_2.fq.gz'

alignment=$base_name'.sam'
report=$base_name'_report.txt'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq'
unmapped_paired=$base_name'_unmapped_paired.fq'

$bw2_dir'bowtie2' --very-sensitive -p 32 -x $base_name -1 $p1_1 -2 $p1_2 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $alignment 2> $report



bw2_dir='/home/kika/miniconda3/pkgs/bowtie2-2.3.4.2-py36h2d50403_0/bin/'
base_name='/media/4TB1/diplonema/mapping/RNA_to_transcriptomes/1610/1610_RNA_full_bw2'
ref='/media/4TB1/diplonema/transcriptomes/1610_Trinity.fasta'
$bw2_dir'bowtie2-build' --threads 32 $ref $base_name

read_dir='/media/4TB1/diplonema/reads/transcriptome/trimmed/'
p1_1=$read_dir'1610_trimmed_1.fq.gz'
p1_2=$read_dir'1610_trimmed_2.fq.gz'

alignment=$base_name'.sam'
report=$base_name'_report.txt'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq'
unmapped_paired=$base_name'_unmapped_paired.fq'

$bw2_dir'bowtie2' --very-sensitive -p 32 -x $base_name -1 $p1_1 -2 $p1_2 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $alignment 2> $report



bw2_dir='/home/kika/miniconda3/pkgs/bowtie2-2.3.4.2-py36h2d50403_0/bin/'
base_name='/media/4TB1/diplonema/mapping/RNA_to_transcriptomes/1621/1621_RNA_full_bw2'
ref='/media/4TB1/diplonema/transcriptomes/1621_Trinity.fasta'
$bw2_dir'bowtie2-build' --threads 32 $ref $base_name

read_dir='/media/4TB1/diplonema/reads/transcriptome/trimmed/'
p1_1=$read_dir'1621_trimmed_1.fq.gz'
p1_2=$read_dir'1621_trimmed_2.fq.gz'

alignment=$base_name'.sam'
report=$base_name'_report.txt'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq'
unmapped_paired=$base_name'_unmapped_paired.fq'

$bw2_dir'bowtie2' --very-sensitive -p 32 -x $base_name -1 $p1_1 -2 $p1_2 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $alignment 2> $report
