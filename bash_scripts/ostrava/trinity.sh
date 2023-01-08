#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N trinity
#PBS -l nodes=1:ppn=80
#PBS -l walltime=100:00:00


cd '/mnt/data/kika/blastocrithidia/transcriptomes/b_spHR05/trinity/'

reads='/mnt/data/kika/blastocrithidia/transcriptomes/b_spHR05/reads/'
fwd=$reads'braa_trimmed_1.fq.gz'
rev=$reads'braa_trimmed_2.fq.gz'

genome_dir='/mnt/data/kika/blastocrithidia/genomes/final_assemblies/'
genome=$genome_dir'Braa_genome_final_corrected2_masked.fa'
species='Braa'

Trinity --seqType fq --left $fw --right $rv --max_memory 100G --CPU 50

gmap_build -D $genome_dir -d $species'_gmap' $genome
gmap -D $genome_dir -d $species'_gmap' -B 4 -t 50 -f gff3_match_cdna Trinity.fasta > Trinity.gff3


python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: Trinity done
