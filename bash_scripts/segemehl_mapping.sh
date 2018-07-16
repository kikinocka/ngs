#!/bin/bash

tools='/home/kika/tools/'

data_dir='/media/4TB1/diplonema/mapping/segemehl/1604/'
database=$data_dir'additional_contigs_se_polyT.fa'
index=$data_dir'additional_contigs_se_polyT.idx'
# ctga_index=$data_dir'additional_contigs.ctgaidx'

read_dir='/media/4TB1/diplonema/reads/transcriptome/trimmed/'
fwd=$read_dir'1604_trimmed_1_se.fq.gz'
rv=$read_dir'1604_trimmed_2_se.fq.gz'

$tools'segemehl_diplonema.x' -d $database -x $index -t 32
$tools'segemehl_diplonema.x' -d $database -x $ctga_index -F 5 -t 32

base_name=$data_dir'1604_segemehl-S-F6'
samfile=$base_name'.sam'
gzip_sam=$samfile'.gz'
unmapped=$base_name'_unmapped.fq'
report=$base_name'_report.txt'
bamfile=$base_name'_sorted.bam'
trans_file=$base_name'_trans.bed'
split_file=$base_name'_split.bed'

#split-read mapping in mode -F 6
$tools'segemehl_diplonema.x' -d $database -i $index -q $fwd -p $rv -o $samfile -t 32 -s -S -F 6 -u $unmapped 2> $report
samtools view -bS $samfile | samtools sort -o $bamfile 
samtools index $bamfile
rm -f $samfile
gzip -f $unmapped
samtools view -h $bamfile | gzip -c > $gzip_sam
./testrealign.x -d $database -q $gzip_sam -n -T $trans_file -U $split_file
