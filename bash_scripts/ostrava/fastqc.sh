#!/bin/bash
#PBS -N fastqc
#PBS -l nodes=1:ppn=5
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cd '/mnt/data/kika/blastocrithidia/o_eliasi/reads/'
fwd='PNG74_trimmed_1.fq.gz'
rev='PNG74_trimmed_2.fq.gz'
report='oeli_trimmed.fastqc.txt'

# fastqc -o ./fastqc -t 5 *.fq 2> $report
fastqc -o ./fastqc -t 5 $fwd $rev 2> $report
