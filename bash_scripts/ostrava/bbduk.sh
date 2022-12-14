#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N bbduk
#PBS -l nodes=1:ppn=10
#PBS -l walltime=02:00:00

bbduk='/home/users/kika/bbmap/bbduk.sh'
adapt='/home/users/kika/bbmap/resources/adapters.fa'

cd '/mnt/data/kika/blastocrithidia/transcriptomes/o_volfi/reads/'
fwd='CC37A_1.fastq.gz'
rev='CC37A_2.fastq.gz'
trimmed_fwd='ovol_trimmed_1.fq.gz'
trimmed_rev='ovol_trimmed_2.fq.gz'
report='ovol_bbduk.txt'
len=50

#illumina pair-end reads
$bbduk overwrite=true \
	in1=$fwd in2=$rev \
	out1=$trimmed_fwd out2=$trimmed_rev \
	ref=$adapt \
	minlen=$len \
	qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=10 2> $report

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: bbduk done
