#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N bbduk
#PBS -l nodes=1:ppn=10
#PBS -l walltime=02:00:00

adapt='/home/users/kika/bbmap/resources/adapters.fa'

cd '/mnt/data/kika/blastocrithidia/transcriptomes/b_triatomae/reads/'
fwd='Blastoc_triat_1.fastq.gz'
rev='Blastoc_triat_2.fastq.gz'
trimmed_fwd='triat_trimmed_1.fq.gz'
trimmed_rev='triat_trimmed_2.fq.gz'
report='btri_bbduk.txt'
len=50

#illumina pair-end reads
/home/users/kika/bbmap/bbduk.sh overwrite=true \
	in1=$fwd in2=$rev \
	out1=$trimmed_fwd out2=$trimmed_rev \
	ref=$adapt \
	minlen=$len \
	qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=10 2> $report
