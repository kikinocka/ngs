#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N qualimap
#PBS -l nodes=1:ppn=20
#PBS -l walltime=100:00:00


name='Bfru'
bam='/mnt/data/kika/blastocrithidia/genomes/final_bw2/'$name'_bw2_sorted.bam'
outdir='/mnt/data/kika/blastocrithidia/genomes/final_assemblies/qualimap/'

qualimap bamqc -bam $bam -nt 20 -outdir $outdir -outformat pdf

mv 'genome_results.txt' $name'_genome_results.txt'
mv 'report.pdf' $name'_report.pdf'

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: qualimap done
