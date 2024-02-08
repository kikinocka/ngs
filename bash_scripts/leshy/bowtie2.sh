#!/bin/bash

cd '/mnt/mokosz/home/kika/egracilis/EG_AK_bw2/'
assembly_dir='/mnt/mokosz/home/zoli/proj/Euglena_Ania/'
read_dir='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/'

base_name='EG_AK_bw2'
ref=$assembly_dir'E.gracilis_genome_Ania.fasta'
cpu=20

p1_1=$read_dir'SRR2094880_trimmed_1.fq.gz'
p2_1=$read_dir'SRR2094885_trimmed_1.fq.gz'
p3_1=$read_dir'SRR2094888_trimmed_1.fq.gz'
p4_1=$read_dir'SRR2094891_trimmed_1.fq.gz'
p5_1=$read_dir'SRR3195329_trimmed_1.fq.gz'
p6_1=$read_dir'SRR3195334_trimmed_1.fq.gz'
p7_1=$read_dir'SRR3195339_trimmed_1.fq.gz'
p8_1=$read_dir'SRR2094881_trimmed_1.fq.gz'
p9_1=$read_dir'SRR2094886_trimmed_1.fq.gz'
p10_1=$read_dir'SRR2094889_trimmed_1.fq.gz'
p11_1=$read_dir'SRR3195326_trimmed_1.fq.gz'
p12_1=$read_dir'SRR3195331_trimmed_1.fq.gz'
p13_1=$read_dir'SRR3195335_trimmed_1.fq.gz'
p14_1=$read_dir'SRR3195340_trimmed_1.fq.gz'
p15_1=$read_dir'SRR2094882_trimmed_1.fq.gz'
p16_1=$read_dir'SRR2094887_trimmed_1.fq.gz'
p17_1=$read_dir'SRR2094890_trimmed_1.fq.gz'
p18_1=$read_dir'SRR3195327_trimmed_1.fq.gz'
p19_1=$read_dir'SRR3195332_trimmed_1.fq.gz'
p20_1=$read_dir'SRR3195338_trimmed_1.fq.gz'

p1_2=$read_dir'SRR2094880_trimmed_2.fq.gz'
p2_2=$read_dir'SRR2094885_trimmed_2.fq.gz'
p3_2=$read_dir'SRR2094888_trimmed_2.fq.gz'
p4_2=$read_dir'SRR2094891_trimmed_2.fq.gz'
p5_2=$read_dir'SRR3195329_trimmed_2.fq.gz'
p6_2=$read_dir'SRR3195334_trimmed_2.fq.gz'
p7_2=$read_dir'SRR3195339_trimmed_2.fq.gz'
p8_2=$read_dir'SRR2094881_trimmed_2.fq.gz'
p9_2=$read_dir'SRR2094886_trimmed_2.fq.gz'
p10_2=$read_dir'SRR2094889_trimmed_2.fq.gz'
p11_2=$read_dir'SRR3195326_trimmed_2.fq.gz'
p12_2=$read_dir'SRR3195331_trimmed_2.fq.gz'
p13_2=$read_dir'SRR3195335_trimmed_2.fq.gz'
p14_2=$read_dir'SRR3195340_trimmed_2.fq.gz'
p15_2=$read_dir'SRR2094882_trimmed_2.fq.gz'
p16_2=$read_dir'SRR2094887_trimmed_2.fq.gz'
p17_2=$read_dir'SRR2094890_trimmed_2.fq.gz'
p18_2=$read_dir'SRR3195327_trimmed_2.fq.gz'
p19_2=$read_dir'SRR3195332_trimmed_2.fq.gz'
p20_2=$read_dir'SRR3195338_trimmed_2.fq.gz'

samfile=$base_name'.sam'
report=$base_name'.report.txt'
bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

bowtie2-build --threads $cpu $ref $base_name
bowtie2 --very-sensitive -p $cpu \
	-x $base_name \
	-1 $p1_1,$p2_1,$p3_1,$p4_1,$p5_1,$p6_1,$p7_1,$p8_1,$p9_1,$p10_1,$p11_1,$p12_1,$p13_1,$p14_1,$p15_1,$p16_1,$p17_1,$p18_1,$p19_1,$p20_1 \
	-2 $p1_2,$p2_2,$p3_2,$p4_2,$p5_2,$p6_2,$p7_2,$p8_2,$p9_2,$p10_2,$p11_2,$p12_2,$p13_2,$p14_2,$p15_2,$p16_2,$p17_2,$p18_2,$p19_2,$p20_2 \
	--no-unal \
	-S $samfile 2> $report

samtools view -bS $samfile > $bamfile -@ $cpu 
samtools sort -o $sorted -@ $cpu $bamfile 
samtools index $sorted


python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py Bowtie2 done
