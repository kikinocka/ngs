#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N hisat2
#PBS -l nodes=1:ppn=80
#PBS -l walltime=999:00:00


cd '/mnt/data/kika/blastocrithidia/transcriptomes/b_spHR05/'

genome='/mnt/data/kika/blastocrithidia/genomes/final_assemblies/Braa_genome_final_masked.fa'
fw='reads/braa_trimmed_1.fq.gz'
rv='reads/braa_trimmed_2.fq.gz'
index='braa_ht2'
unmapped_unpaired=$index'_unmapped_unpaired.fq.gz'
unmapped_paired=$index'_unmapped_paired.fq.gz'
sam=$index'.sam'
report=$index'_report.txt'
bam=$index'_unsorted.bam'
sorted=$index'_sorted.bam'

hisat2-build -p 20 $genome $index
hisat2 --very-sensitive -p 50 \
	--dta --secondary \
	-x $index \
	-1 $fw \
	-2 $rv \
	--un-gz $unmapped_unpaired \
	--un-conc-gz $unmapped_paired \
	-S $sam 2> $report
#--dta 			reports alignments tailored for transcript assemblers
#--secondary	reports secondary alignments

# samtools view -bS -F 4 $sam > $bam -@ 20 #writes only mapped reads to bamfile
samtools view -bS $sam > $bam -@ 20
samtools sort -o $sorted -@ 20 $bam 
samtools index $sorted

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: hisat2 done
