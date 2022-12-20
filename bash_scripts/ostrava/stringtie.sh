#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N strigtie
#PBS -l nodes=1:ppn=50
#PBS -l walltime=100:00:00


cd '/mnt/data/kika/blastocrithidia/'

stringtie='/home/users/kika/stringtie/stringtie'
bam='transcriptomes/b_triatomae/hisat2/btri_ht2_sorted.bam'
gtf='transcriptomes/b_triatomae/stringtie/Btri_ST.gtf'
gff='transcriptomes/b_triatomae/stringtie/Btri_ST.gff'
gff_transcripts='transcriptomes/b_triatomae/stringtie/Btri_ST_transcripts.gff'
out='transcriptomes/b_triatomae/stringtie/Btri_ST.fa'
genome='genomes/final_assemblies/Btri_genome_final_masked.fa'

$stringtie -v -o $gtf $bam -m 50 -p 30
#-m 	minimum assembled transcript length (default: 200)

gffread $gtf -o $gff
grep 'transcript' $gff > $gff_transcripts
bedtools getfasta -fi $genome -bed $gff_transcripts -fo $out

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: StringTie done
