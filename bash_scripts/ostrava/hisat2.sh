#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N hisat2
#PBS -l nodes=1:ppn=20
#PBS -l walltime=50:00:00


cd '/mnt/data/kika/blastocrithidia/transcriptomes/o_volfi/'

genome='/mnt/data/kika/blastocrithidia/genomes/final_assemblies/Ovol_genome_final.fa'
fw='reads/ovol_trimmed_1.fq.gz'
rv='reads/ovol_trimmed_1.fq.gz'
index='ovol_ht2'
unmapped_unpaired=$index'_unmapped_unpaired.fq.gz'
unmapped_paired=$index'_unmapped_paired.fq.gz'
sam=$index'.sam'
report=$index'_report.txt'
bam=$index'_unsorted.bam'
sorted=$index'_sorted.bam'

hisat2-build -p 20 $genome $index
hisat2 -p 20 -x $index -1 $fw -2 $rv --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $sam 2> $report

# samtools view -bS -F 4 $sam > $bam -@ 20 #writes only mapped reads to bamfile
samtools view -bS $sam > $bam -@ 20
samtools sort -o $sorted -@ 20 $bam 
samtools index $sorted

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSTRAVA: hisat2 done
