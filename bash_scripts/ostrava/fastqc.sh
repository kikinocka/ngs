#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N fastqc
#PBS -l nodes=1:ppn=5
#PBS -l walltime=02:00:00


cd '/home/users/kika/bnon_pfr_ko/reads/'
# fwd='4FEM_trimmed_75_1.fq'
# rev='4FEM_trimmed_75_2.fq'
report='bnon_PF16_KO.fastqc.txt'

fastqc -o ./fastqc -t 5 *.gz 2> $report
# fastqc -o ./fastqc -t 5 $fwd $rev 2> $report

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: FASTQC done
