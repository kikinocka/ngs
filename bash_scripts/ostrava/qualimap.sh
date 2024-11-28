#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N qualimap
#PBS -l nodes=1:ppn=20
#PBS -l walltime=100:00:00


name='Oeli'
bam='/mnt/data/kika/blastocrithidia/genomes/final_bw2/'$name'_bw2_sorted.bam'
outdir='/mnt/data/kika/blastocrithidia/genomes/final_assemblies/qualimap/'

qualimap bamqc -bam $bam -nt 20 -outdir $outdir -outformat pdf

mv $outdir'genome_results.txt' $outdir$name'_genome_results.txt'
mv $outdir'report.pdf' $outdir$name'_report.pdf'

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: qualimap done
