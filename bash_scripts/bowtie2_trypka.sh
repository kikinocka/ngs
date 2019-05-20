#!/bin/bash

bw2_dir='/home/kika/miniconda3/pkgs/bowtie2-2.3.4.2-py36h2d50403_0/bin/'
base_name='/media/4TB1/blastocrithidia/mapping/lmex_ku80_bowtie2_DNA/lmex_ku80_bw2'
ref='/media/4TB1/blastocrithidia/genome_assembly/ku_mutants/Lmex_Ku80/scaffolds.fasta'

$bw2_dir'bowtie2-build' --threads 32 $ref $base_name

read_dir='/media/4TB1/blastocrithidia/reads/ku_mutants/'
p1_1=$read_dir'Lmex_Ku80_trimmed_1.fq.gz'
p1_2=$read_dir'Lmex_Ku80_trimmed_2.fq.gz'

samfile=$base_name'.sam'
report=$base_name'_report.txt'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq'
unmapped_paired=$base_name'_unmapped_paired.fq'

bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

$bw2_dir'bowtie2' --very-sensitive -p 32 -x $base_name \
-1 $p1_1 -2 $p1_2 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $samfile 2> $report

samtools view -bS $samfile > $bamfile -@ 32
samtools sort -o $sorted -@ 32 $bamfile
samtools index -b $sorted
