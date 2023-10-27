#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N gffread
#PBS -l nodes=1:ppn=10
#PBS -l walltime=900:00:00

cd '/home/users/kika/bnon_pfr_ko/'
gff='bnon_proteins_annotated.gff3'
gtf='bnon_proteins_annotated.gtf'

gffread $gff -T -o $gtf

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: gffread done
