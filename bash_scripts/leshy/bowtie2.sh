#!/bin/bash

cd '/mnt/mokosz/home/kika/egracilis/EG_AK_bw2/'
assembly_dir='/mnt/mokosz/home/kika/egracilis/PacBio/'
read_dir='/mnt/mokosz/home/kika/egracilis/PacBio/hifi_reads/'

base_name='EG_hifi_bw2'
ref=$assembly_dir'EG_hifi.asm.p_ctg.fa'
cpu=20

p1_1=$read_dir'EG_hifi.fastq.gz'
# p1_2=$read_dir'SRR2094880_trimmed_2.fq.gz'

samfile=$base_name'.sam'
report=$base_name'.report.txt'
mapped=$base_name'_mapped.fq.gz'
# unmapped_unpaired=$base_name'_unmapped_unpaired.fq.gz'
# unmapped_paired=$base_name'_unmapped_paired.fq.gz'
unaligned=$base_name'_unaligned.fq.gz'
report=$base_name'.report.txt'
bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

bowtie2-build --threads $cpu $ref $base_name

# #paired-end reads
# bowtie2 --very-sensitive -p $cpu \
# 	-x $base_name \
# 	-1 $p1_1 \
# 	-2 $p1_2 \
# 	--un-gz $unmapped_unpaired \
# 	--un-conc-gz $unmapped_paired \
# 	--al-conc-gz $mapped \
# 	-S $samfile 2> $report

#single reads
bowtie2 --very-sensitive -p $cpu \
	-x $base_name \
	-U $p1_1 \
	--al-gz $mapped \
	--un-gz $unaligned \
	-S $samfile 2> $report

samtools view -bS $samfile > $bamfile -@ $cpu 
samtools sort -o $sorted -@ $cpu $bamfile 
samtools index $sorted


python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py Bowtie2 done
