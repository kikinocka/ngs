#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N hisat2
#PBS -l nodes=1:ppn=50
#PBS -l walltime=100:00:00


cd '/mnt/data/kika/blastocrithidia/'

stringtie='/home/users/kika/stringtie/stringtie'
bam='transcriptomes/b_spHR05/hisat2/braa_ht2_sorted.bam'
gtf='transcriptomes/b_spHR05/stringtie/Braa_ST.gtf'
out='transcriptomes/b_spHR05/stringtie/Braa_ST.fa'
genome='genomes/final_assemblies/Braa_genome_final_masked.fa'

$stringtie -v -o $gtf $bam -m 50 -p 30
#-m 	minimum assembled transcript length (default: 200)

bedtools getfasta -fi $genome -bed $gtf -fo $out -name

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: StringTie done