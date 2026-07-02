#!/bin/bash

cd '/mnt/mokosz/home/kika/egracilis/chinese/'

genome='GCA_039621445.1_ASM3962144v1_genomic.fna'

fw1='RNA_reads/SRR17465011_trimmed_1.fq.gz'
fw2='RNA_reads/SRR17465012_trimmed_1.fq.gz'

rv1='RNA_reads/SRR17465011_trimmed_2.fq.gz'
rv2='RNA_reads/SRR17465012_trimmed_2.fq.gz'

index='EG_control_ht2'
unmapped_unpaired=$index'_unmapped_unpaired.fq.gz'
unmapped_paired=$index'_unmapped_paired.fq.gz'
sam=$index'.sam'
report=$index'.report.txt'
bam=$index'.unsorted.bam'
sorted=$index'.sorted.bam'

hisat2-build -p 20 $genome $index
hisat2 -p 15 -x $index \
	-1 $fw1,$fw2 \
	-2 $rv1,$rv2 \
 	--un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $sam 2> $report

samtools view -bS $sam > $bam -@ 20
samtools sort -o $sorted -@ 20 $bam 
samtools index $sorted


python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py Hisat2 done
