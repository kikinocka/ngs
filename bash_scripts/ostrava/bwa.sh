#!/bin/bash
#SBATCH --job-name=bwa
#SBATCH --output=bwa.%j.out
#SBATCH --error=bwa.%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=50
#SBATCH --time=10:00:00
#SBATCH --export=ALL

cd '/home/kika/pkld/bwa/'

ref='Ldon_GCF_000227135.1.fna'
p1_1='trimmed_all/karect_BHU814_trimmed_1.fq.gz'
p1_2='trimmed_all/karect_BHU814_trimmed_2.fq.gz'
base_name='BHU814_bwa'
samfile=$base_name'.sam'
report=$base_name'.report.txt'
bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'
statsfile=$base_name'_stats.txt'


# bwa index $ref

bwa mem -t 50 $ref $p1_1 $p1_2 > $samfile 2> $report

# samtools view -bS -F 4 -@ 50 $samfile > $bamfile #writes only mapped reads to bamfile
samtools view -bS -@ 50 $samfile > $bamfile
samtools sort -o $sorted -@ 50 $bamfile 
samtools index -b $sorted
samtools stats $sorted | grep ^SN > $statsfile
