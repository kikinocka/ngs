#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N strigtie
#PBS -l nodes=1:ppn=50
#PBS -l walltime=100:00:00


cd '/mnt/data/kika/blastocrithidia/'

stringtie='/home/users/kika/stringtie/stringtie'
bam='transcriptomes/b_frustrata/hisat2/bfru_ht2_sorted.bam'
gtf='transcriptomes/b_frustrata/stringtie/Bfru_ST.gtf'
out='transcriptomes/b_frustrata/stringtie/Bfru_ST.fa'
genome='genomes/final_assemblies/Bfru_genome_final_masked.fa'

$stringtie -v -o $gtf $bam -m 50 -p 30
#-m 	minimum assembled transcript length (default: 200)

bedtools getfasta -fi $genome -bed $gff -fo $out -name

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: StringTie done
