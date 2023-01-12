#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N gmap
#PBS -l nodes=1:ppn=20
#PBS -l walltime=100:00:00


cd '/mnt/data/kika/blastocrithidia/transcriptomes/o_volfi/trinity/'

genome='/mnt/data/kika/blastocrithidia/genomes/final_assemblies/Ovol_genome_final_masked.fa'
species='ovol'

gmap_build -D . -d $species'_gmap' $genome
gmap -D . -d $species'_gmap' -B 4 -t 20 -f gff3_match_cdna Trinity.fasta > Trinity_gmap.gff3

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: gmap done
