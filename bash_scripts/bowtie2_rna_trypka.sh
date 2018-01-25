#!/bin/bash

bw2_dir='/home/nenarokova/tools/bowtie2-2.2.9/'
base_name='/media/4TB1/blasto/mapping/p57_bw2'
ref="/home/nenarokova/genomes/blasto/blastocrithidia/genome/p57_scaffolds.fa"
$bw2_dir'bowtie2-build' --threads 32 $ref $base_name

p1_1="/home/kika/blastocrithidia/transcriptome/trimmed/p57_trimmed_1.fq.gz"
p1_2="/home/kika/blastocrithidia/transcriptome/trimmed/p57_trimmed_2.fq.gz"

alignment=$base_name".sam"
report=$base_name".txt"
unmapped_unpaired=$base_name"_unmapped_unpaired.fq"
unmapped_paired=$base_name"_unmapped_paired.fq"

$bw2_dir'bowtie2' --very-sensitive -p 20 -x $base_name -1 $p1_1 -2 $p1_2 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $alignment 2> $report

samfile=$alignment
bamfile=$base_name"_unsorted.bam"
sorted=$base_name"_sorted"
sorted_file=$sorted".bam"

samtools view -bS $samfile > $bamfile -@ 20
samtools sort $bamfile $sorted -@ 20
samtools index $sorted_file

