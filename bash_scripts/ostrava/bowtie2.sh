#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N bowtie2
#PBS -l nodes=1:ppn=80
#PBS -l walltime=600:00:00

cd '/home/users/kika/bnon_KOs/catalase/'

ref='/home/users/kika/bnon_KOs/p57_polished.fa'
p1_1='reads/cat_KO.trimmed_1.fq.gz'
p1_2='reads/cat_KO.trimmed_2.fq.gz'
base_name='bw2_mapping/cat_KO.bw2'
samfile=$base_name'.sam'
mapped=$base_name'_mapped.fq.gz'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq.gz'
unmapped_paired=$base_name'_unmapped_paired.fq.gz'
report=$base_name'.report.txt'
bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'


eval "$(/home/users/kika/miniconda3/bin/conda shell.bash hook)"
conda activate bowtie2

bowtie2-build $ref $base_name

#paired-end reads
bowtie2 --very-sensitive -p 50 \
	-x $base_name \
	-1 $p1_1 \
	-2 $p1_2 \
	--un-gz $unmapped_unpaired \
	--un-conc-gz $unmapped_paired \
	--al-conc-gz $mapped \
	-S $samfile 2> $report
	# -U $r1,$r2 \
	#--no-unal \ #writes only mapped reads to sam file


# samtools view -bS -F 4 $samfile > $bamfile -@ 50 #writes only mapped reads to bamfile
samtools view -bS -@ 50 $samfile > $bamfile
samtools sort -o $sorted -@ 50 $bamfile 
samtools index -b $sorted

conda deactivate


python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: bowtie2 done
