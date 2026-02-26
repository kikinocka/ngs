#!/bin/bash
#SBATCH --job-name=bowtie2
#SBATCH --output=bowtie2.%j.out
#SBATCH --error=bowtie2.%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=50
#SBATCH --time=02:00:00
#SBATCH --export=ALL

cd '/home/kika/pkld/'

ref='references/Ldon_GCF_000227135.1.fna'
p1_1='trimmed_all/karect_PKD1-SC-SP_trimmed_1.fq.gz'
p1_2='trimmed_all/karect_PKD1-SC-SP_trimmed_2.fq.gz'
base_name='PKD1-SC-SP_bw2'
samfile=$base_name'.sam'
mapped=$base_name'_mapped.fq.gz'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq.gz'
unmapped_paired=$base_name'_unmapped_paired.fq.gz'
report=$base_name'.report.txt'
bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'


bowtie2-build $ref $base_name

#paired-end reads
bowtie2 --end-to-end --very-sensitive --no-discordant -p 50 \
	-x $base_name \
	-1 $p1_1 \
	-2 $p1_2 \
	--un-gz $unmapped_unpaired \
	--un-conc-gz $unmapped_paired \
	--al-conc-gz $mapped \
	-S $samfile 2> $report
	# -U $r1,$r2 \
	#--no-unal \ #writes only mapped reads to sam file

# samtools view -bS -F 4 -@ 50 $samfile > $bamfile #writes only mapped reads to bamfile
samtools view -bS -@ 50 $samfile > $bamfile
samtools sort -o $sorted -@ 50 $bamfile 
samtools index -b $sorted

