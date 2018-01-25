#!/bin/bash

bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
read_dir='/media/4TB1/blastocrithidia/bexlh/reads/trimmed/PRJNA284294/'
base_name='/media/4TB1/blastocrithidia/mapping/lhes2_bowtie2_RNA/lhes2_bw2'
ref='/media/4TB1/blastocrithidia/bexlh/lhes2_PRJNA284294_trinity/Trinity.fasta'
$bw2_dir'bowtie2-build' --threads 32 $ref $base_name

p1_1=$read_dir'SRR2170108_trimmed_1.fq.gz',$read_dir'SRR2170117_trimmed_1.fq.gz',$read_dir'SRR2173361_trimmed_1.fq.gz'
p1_2=$read_dir'SRR2170108_trimmed_2.fq.gz',$read_dir'SRR2170117_trimmed_2.fq.gz',$read_dir'SRR2173361_trimmed_2.fq.gz'

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