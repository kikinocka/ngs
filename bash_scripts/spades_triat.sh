#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=32

pe1_1="/home/nenarokova/genomes/blasto/blastocrithidia/genome/trimmed/triat_trimmed_1.fq"
pe1_2="/home/nenarokova/genomes/blasto/blastocrithidia/genome/trimmed/triat_trimmed_2.fq"

outdir="/home/nenarokova/genomes/blasto/blastocrithidia/genome/assembly/triat/"

report=$outdir"spades_report.txt"

/home/nenarokova/tools/SPAdes-3.9.0-Linux/bin/spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 --careful -t 32 -o $outdir
