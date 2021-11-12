#!/bin/bash

cd '/mnt/mokosz/home/zoli/proj/Euglena_v2/hisat2_mapping/'

genome='/mnt/mokosz/home/zoli/proj/Euglena_v2/genome.fasta'

fw1='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094880_trimmed_1.fq.gz'
fw2='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094886_trimmed_1.fq.gz'
fw3='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094890_trimmed_1.fq.gz'
fw4='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195329_trimmed_1.fq.gz'
fw5='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195335_trimmed_1.fq.gz'
fw6='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094881_trimmed_1.fq.gz'
fw7='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094887_trimmed_1.fq.gz'
fw8='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094891_trimmed_1.fq.gz'
fw9='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195331_trimmed_1.fq.gz'
fw10='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195338_trimmed_1.fq.gz'
fw11='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094882_trimmed_1.fq.gz'
fw12='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094888_trimmed_1.fq.gz'
fw13='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195326_trimmed_1.fq.gz'
fw14='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195332_trimmed_1.fq.gz'
fw15='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195339_trimmed_1.fq.gz'
fw16='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094885_trimmed_1.fq.gz'
fw17='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094889_trimmed_1.fq.gz'
fw18='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195327_trimmed_1.fq.gz'
fw19='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195334_trimmed_1.fq.gz'
fw20='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195340_trimmed_1.fq.gz'

rv1='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094880_trimmed_2.fq.gz'
rv2='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094886_trimmed_2.fq.gz'
rv3='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094890_trimmed_2.fq.gz'
rv4='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195329_trimmed_2.fq.gz'
rv5='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195335_trimmed_2.fq.gz'
rv6='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094881_trimmed_2.fq.gz'
rv7='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094887_trimmed_2.fq.gz'
rv8='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094891_trimmed_2.fq.gz'
rv9='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195331_trimmed_2.fq.gz'
rv10='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195338_trimmed_2.fq.gz'
rv11='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094882_trimmed_2.fq.gz'
rv12='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094888_trimmed_2.fq.gz'
rv13='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195326_trimmed_2.fq.gz'
rv14='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195332_trimmed_2.fq.gz'
rv15='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195339_trimmed_2.fq.gz'
rv16='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094885_trimmed_2.fq.gz'
rv17='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR2094889_trimmed_2.fq.gz'
rv18='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195327_trimmed_2.fq.gz'
rv19='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195334_trimmed_2.fq.gz'
rv20='/mnt/mokosz/home/zoli/proj/Euglena_v2/reads/SRR3195340_trimmed_2.fq.gz'

index='egr_ht2'
unmapped_unpaired=$index'_unmapped_unpaired.fq.gz'
unmapped_paired=$index'_unmapped_paired.fq.gz'
sam=$index'.sam'
report=$index'_report.txt'
bam=$index'_unsorted.bam'
sorted=$index'_sorted.bam'

hisat2-build -p 10 $genome $index
hisat2 -p 10 -x $index \
	-1 $fw1,$fw2,$fw3,$fw4,$fw5,$fw6,$fw7,$fw8,$fw9,$fw10,$fw11,$fw12,$fw13,$fw14,$fw15,$fw16,$fw17,$fw18,$fw19,$fw20 \
	-2 $rv1,$rv2,$rv3,$rv4,$rv5,$rv6,$rv7,$rv8,$rv9,$rv10,$rv11,$rv12,$rv13,$rv14,$rv15,$rv16,$rv17,$rv18,$rv19,$rv20 \
 	--un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $sam 2> $report

samtools view -bS $sam > $bam -@ 10
samtools sort -o $sorted -@ 10 $bam 
samtools index $sorted

