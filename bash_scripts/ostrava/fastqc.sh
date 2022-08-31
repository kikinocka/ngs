#!/bin/bash
#PBS -N fastqc
#PBS -l nodes=1:ppn=5
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cd '/mnt/data/kika/blastocrithidia/b_triatomae/reads/'
fwd='karect_triat_trimmed_75_1.fq'
rev='karect_triat_trimmed_75_2.fq'
report='karect_triat_trimmed_75.fastqc.txt'

fastqc -o ./fastqc -t 5 $fwd $rev 2> $report
