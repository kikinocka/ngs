#!/bin/bash

bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
base_name='/media/4TB1/blastocrithidia/mapping/p57_polyA_RNA_to_DNA/p57_polyA_bw2'
ref='/media/4TB1/blastocrithidia/genome_assembly/p57_scaffolds.fa'
$bw2_dir'bowtie2-build' --threads 32 $ref $base_name

read_dir='/media/4TB1/blastocrithidia/reads/transcriptome/trimmed/'
p1_1=$read_dir'p57_3-end_enriched_trimmed_1.fq.gz'
p1_2=$read_dir'p57_3-end_enriched_trimmed_1.fq.gz'

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