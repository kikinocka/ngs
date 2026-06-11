#!/bin/bash

cd '/mnt/mokosz/home/kika/egracilis/chinese/'

genome='GCA_039621445.1_ASM3962144v1_genomic.fna'

fw1='reads/SRR17465006_trimmed_1.fq.gz'
fw2='reads/SRR17465007_trimmed_1.fq.gz'
fw3='reads/SRR17465008_trimmed_1.fq.gz'
fw4='reads/SRR17465009_trimmed_1.fq.gz'
fw5='reads/SRR17465010_trimmed_1.fq.gz'
fw6='reads/SRR17465011_trimmed_1.fq.gz'
fw7='reads/SRR17465012_trimmed_1.fq.gz'
fw8='reads/SRR17465013_trimmed_1.fq.gz'
fw9='reads/SRR17465014_trimmed_1.fq.gz'
fw10='reads/SRR17465015_trimmed_1.fq.gz'
fw11='reads/SRR17465016_trimmed_1.fq.gz'
fw12='reads/SRR17465017_trimmed_1.fq.gz'
fw13='reads/SRR17465018_trimmed_1.fq.gz'
fw14='reads/SRR17465019_trimmed_1.fq.gz'
fw15='reads/SRR17465020_trimmed_1.fq.gz'
fw16='reads/SRR17465021_trimmed_1.fq.gz'
fw17='reads/SRR17465022_trimmed_1.fq.gz'
fw18='reads/SRR17465023_trimmed_1.fq.gz'
fw19='reads/SRR17465024_trimmed_1.fq.gz'
fw20='reads/SRR17465025_trimmed_1.fq.gz'
fw21='reads/SRR17465026_trimmed_1.fq.gz'
fw22='reads/SRR17465027_trimmed_1.fq.gz'
fw23='reads/SRR17465028_trimmed_1.fq.gz'
fw24='reads/SRR17465029_trimmed_1.fq.gz'
fw25='reads/SRR17465030_trimmed_1.fq.gz'

rv1='reads/SRR17465006_trimmed_2.fq.gz'
rv2='reads/SRR17465007_trimmed_2.fq.gz'
rv3='reads/SRR17465008_trimmed_2.fq.gz'
rv4='reads/SRR17465009_trimmed_2.fq.gz'
rv5='reads/SRR17465010_trimmed_2.fq.gz'
rv6='reads/SRR17465011_trimmed_2.fq.gz'
rv7='reads/SRR17465012_trimmed_2.fq.gz'
rv8='reads/SRR17465013_trimmed_2.fq.gz'
rv9='reads/SRR17465014_trimmed_2.fq.gz'
rv10='reads/SRR17465015_trimmed_2.fq.gz'
rv11='reads/SRR17465016_trimmed_2.fq.gz'
rv12='reads/SRR17465017_trimmed_2.fq.gz'
rv13='reads/SRR17465018_trimmed_2.fq.gz'
rv14='reads/SRR17465019_trimmed_2.fq.gz'
rv15='reads/SRR17465020_trimmed_2.fq.gz'
rv16='reads/SRR17465021_trimmed_2.fq.gz'
rv17='reads/SRR17465022_trimmed_2.fq.gz'
rv18='reads/SRR17465023_trimmed_2.fq.gz'
rv19='reads/SRR17465024_trimmed_2.fq.gz'
rv20='reads/SRR17465025_trimmed_2.fq.gz'
rv21='reads/SRR17465026_trimmed_2.fq.gz'
rv22='reads/SRR17465027_trimmed_2.fq.gz'
rv23='reads/SRR17465028_trimmed_2.fq.gz'
rv24='reads/SRR17465029_trimmed_2.fq.gz'
rv25='reads/SRR17465030_trimmed_2.fq.gz'

index='EG_chin_ht2'
unmapped_unpaired=$index'_unmapped_unpaired.fq.gz'
unmapped_paired=$index'_unmapped_paired.fq.gz'
sam=$index'.sam'
report=$index'.report.txt'
bam=$index'.unsorted.bam'
sorted=$index'.sorted.bam'

hisat2-build -p 20 $genome $index
hisat2 -p 15 -x $index \
	-1 $fw1,$fw2,$fw3,$fw4,$fw5,$fw6,$fw7,$fw8,$fw9,$fw10,$fw11,$fw12,$fw13,$fw14,$fw15,$fw16,$fw17,$fw18,$fw19,$fw20,$fw21,$fw22,$fw23,$fw24,$fw25 \
	-2 $rv1,$rv2,$rv3,$rv4,$rv5,$rv6,$rv7,$rv8,$rv9,$rv10,$rv11,$rv12,$rv13,$rv14,$rv15,$rv16,$rv17,$rv18,$rv19,$rv20,$rv21,$rv22,$rv23,$rv24,$rv25 \
 	--un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $sam 2> $report

samtools view -bS $sam > $bam -@ 20
samtools sort -o $sorted -@ 20 $bam 
samtools index $sorted


python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py Hisat2 done
