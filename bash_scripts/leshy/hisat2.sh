#!/bin/bash

cd '/mnt/mokosz/home/kika/egracilis/chinese/'

genome='GCA_039621445.1_ASM3962144v1_genomic.fna'

fw1='RNA_eads/SRR17465006_trimmed_1.fq.gz'
fw2='RNA_eads/SRR17465007_trimmed_1.fq.gz'
fw3='RNA_eads/SRR17465008_trimmed_1.fq.gz'
fw4='RNA_eads/SRR17465009_trimmed_1.fq.gz'
fw5='RNA_eads/SRR17465010_trimmed_1.fq.gz'
fw6='RNA_eads/SRR17465011_trimmed_1.fq.gz'
fw7='RNA_eads/SRR17465012_trimmed_1.fq.gz'
fw8='RNA_eads/SRR17465013_trimmed_1.fq.gz'
fw9='RNA_eads/SRR17465014_trimmed_1.fq.gz'
fw10='RNA_reads/SRR17465015_trimmed_1.fq.gz'
fw11='RNA_reads/SRR17465016_trimmed_1.fq.gz'
fw12='RNA_reads/SRR17465017_trimmed_1.fq.gz'
fw13='RNA_reads/SRR17465018_trimmed_1.fq.gz'
fw14='RNA_reads/SRR17465019_trimmed_1.fq.gz'
fw15='RNA_reads/SRR17465020_trimmed_1.fq.gz'
fw16='RNA_reads/SRR17465021_trimmed_1.fq.gz'
fw17='RNA_reads/SRR17465022_trimmed_1.fq.gz'
fw18='RNA_reads/SRR17465023_trimmed_1.fq.gz'
fw19='RNA_reads/SRR17465024_trimmed_1.fq.gz'
fw20='RNA_reads/SRR17465025_trimmed_1.fq.gz'
fw21='RNA_reads/SRR17465026_trimmed_1.fq.gz'
fw22='RNA_reads/SRR17465027_trimmed_1.fq.gz'
fw23='RNA_reads/SRR17465028_trimmed_1.fq.gz'
fw24='RNA_reads/SRR17465029_trimmed_1.fq.gz'
fw25='RNA_reads/SRR17465030_trimmed_1.fq.gz'

rv1='RNA_reads/SRR17465006_trimmed_2.fq.gz'
rv2='RNA_reads/SRR17465007_trimmed_2.fq.gz'
rv3='RNA_reads/SRR17465008_trimmed_2.fq.gz'
rv4='RNA_reads/SRR17465009_trimmed_2.fq.gz'
rv5='RNA_reads/SRR17465010_trimmed_2.fq.gz'
rv6='RNA_reads/SRR17465011_trimmed_2.fq.gz'
rv7='RNA_reads/SRR17465012_trimmed_2.fq.gz'
rv8='RNA_reads/SRR17465013_trimmed_2.fq.gz'
rv9='RNA_reads/SRR17465014_trimmed_2.fq.gz'
rv10='RNA_reads/SRR17465015_trimmed_2.fq.gz'
rv11='RNA_reads/SRR17465016_trimmed_2.fq.gz'
rv12='RNA_reads/SRR17465017_trimmed_2.fq.gz'
rv13='RNA_reads/SRR17465018_trimmed_2.fq.gz'
rv14='RNA_reads/SRR17465019_trimmed_2.fq.gz'
rv15='RNA_reads/SRR17465020_trimmed_2.fq.gz'
rv16='RNA_reads/SRR17465021_trimmed_2.fq.gz'
rv17='RNA_reads/SRR17465022_trimmed_2.fq.gz'
rv18='RNA_reads/SRR17465023_trimmed_2.fq.gz'
rv19='RNA_reads/SRR17465024_trimmed_2.fq.gz'
rv20='RNA_reads/SRR17465025_trimmed_2.fq.gz'
rv21='RNA_reads/SRR17465026_trimmed_2.fq.gz'
rv22='RNA_reads/SRR17465027_trimmed_2.fq.gz'
rv23='RNA_reads/SRR17465028_trimmed_2.fq.gz'
rv24='RNA_reads/SRR17465029_trimmed_2.fq.gz'
rv25='RNA_reads/SRR17465030_trimmed_2.fq.gz'

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
