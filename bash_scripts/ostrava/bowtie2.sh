#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N bowtie2
#PBS -l nodes=1:ppn=20
#PBS -l walltime=600:00:00

work_dir='/mnt/data/kika/blastocrithidia/b_triatomae/'

ref=$work_dir'scaff_gap/Btri.platanus_rnd2_scaffold.l500.gapcloser.fa'
p1_1=$work_dir'reads/triat_trimmed_1.fq'
p1_2=$work_dir'reads/triat_trimmed_2.fq'
base_name='Btri.bw2'

cd $work_dir'mapping/'
samfile=$base_name'.sam'
mapped=$base_name'_mapped.fq.gz'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq.gz'
unmapped_paired=$base_name'_unmapped_paired.fq.gz'
report=$base_name'.report.txt'
bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

bowtie2-build $ref $base_name

#paired-end reads
bowtie2 --very-sensitive -p 20 \
	-x $base_name \
	-1 $p1_1 \
	-2 $p1_2 \
	--un-gz $unmapped_unpaired \
	--un-conc-gz $unmapped_paired \
	--al-conc-gz $mapped \
	-S $samfile 2> $report
	# -U $r1,$r2 \
	#--no-unal \ #writes only mapped reads to sam file


# samtools view -bS -F 4 $samfile > $bamfile -@ 20 #writes only mapped reads to bamfile
samtools view -bS -@ 20 $samfile > $bamfile
samtools sort -o $sorted -@ 20 $bamfile 
samtools index -b $sorted
