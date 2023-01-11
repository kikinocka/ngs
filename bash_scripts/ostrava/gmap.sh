#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N gmap
#PBS -l nodes=1:ppn=20
#PBS -l walltime=100:00:00


cd '/mnt/data/kika/blastocrithidia/transcriptomes/b_spHR05/trinity/'

genome='/mnt/data/kika/blastocrithidia/genomes/final_assemblies/Braa_genome_final_corrected2_masked.fa'
species='braa'

gmap_build -D . -d $species'_gmap' $genome
gmap -D . -d $species'_gmap' -B 4 -t 20 -f gff3_match_cdna Trinity.fasta > Trinity_gmap.gff3

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: gmap done
