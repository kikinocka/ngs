#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N qualimap
#PBS -l nodes=1:ppn=20
#PBS -l walltime=100:00:00


bam='/mnt/data/kika/blastocrithidia/genomes/final_bw2/Btri_bw2_sorted.bam'
outdir='/mnt/data/kika/blastocrithidia/genomes/final_assemblies/qualimap/'

qualimap bamqc -bam $bam -nt 20 -outdir $outdir -outformat pdf
