#!/bin/bash
#PBS -N fastqc
#PBS -l nodes=1:ppn=5
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cd '/mnt/data/kika/blastocrithidia/b_triatomae/reads/'
fwd='triat_trimmed_1.fq.gz'
rev='triat_trimmed_2.fq.gz'
report='triat_trimmed.fastqc.txt'

# fastqc -o ./fastqc -t 5 *.fq 2> $report
fastqc -o ./fastqc -t 5 $fwd $rev 2> $report
