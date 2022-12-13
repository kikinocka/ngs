#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N fastqc
#PBS -l nodes=1:ppn=5
#PBS -l walltime=02:00:00


cd '/mnt/data/kika/blastocrithidia/transcriptomes/o_modryi/reads/'
# fwd='4FEM_trimmed_75_1.fq'
# rev='4FEM_trimmed_75_2.fq'
report='omod_trimmed.fastqc.txt'

fastqc -o ./fastqc -t 5 *.gz 2> $report
fastqc -o ./fastqc -t 5 $fwd $rev 2> $report
