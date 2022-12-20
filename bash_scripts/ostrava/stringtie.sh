#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N strigtie
#PBS -l nodes=1:ppn=50
#PBS -l walltime=100:00:00


cd '/mnt/data/kika/blastocrithidia/'

stringtie='/home/users/kika/stringtie/stringtie'
bam='transcriptomes/o_modryi/hisat2/omod_ht2_sorted.bam'
gtf='transcriptomes/o_modryi/stringtie/Omod_ST.gtf'
gff='transcriptomes/o_modryi/stringtie/Omod_ST.gff'
gff_transcripts='transcriptomes/o_modryi/stringtie/Omod_ST_transcripts.gff'
out='transcriptomes/o_modryi/stringtie/Omod_ST.fa'
genome='genomes/final_assemblies/Omod_genome_final_masked.fa'

$stringtie -v -o $gtf $bam -m 50 -p 30
#-m 	minimum assembled transcript length (default: 200)

gffread $gtf -o $gff
grep 'transcript' $gff > $gff_transcripts
bedtools getfasta -fi $genome -bed $gff_transcripts -fo $out

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: StringTie done
