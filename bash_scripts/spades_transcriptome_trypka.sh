#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l nodes=1:ppn=32

pe1_1="/home/kika/blastocrithidia/transcriptome/trimmed/p57_trimmed_1.fq.gz"
pe1_2="/home/kika/blastocrithidia/transcriptome/trimmed/p57_trimmed_2.fq.gz"

outdir="/home/kika/blastocrithidia/transcriptome/assembly/p57"

report=$outdir"spades_report.txt"

/home/kika/tools/SPAdes-3.9.1-Linux/bin/spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 -t 32 --only-assembler -o $outdir
