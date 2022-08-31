#!/bin/bash
#PBS -N bbduk
#PBS -l nodes=1:ppn=10
#PBS -l walltime=01:00:00
#PBS -m ae
#PBS -j oe


raw_dir='/mnt/data/kika/blastocrithidia/b_triatomae-OLD/genome/reads/'
fwd=$raw_dir'Blastoc_triat_1.fastq.gz'
rev=$raw_dir'Blastoc_triat_2.fastq.gz'

adapt='/home/users/kika/bbmap/resources/adapters.fa'


cd '/mnt/data/kika/blastocrithidia/b_triatomae/reads/'
trimmed_fwd='triat_trimmed_75_1_fq.gz'
trimmed_rev='triat_trimmed_75_2_fq.gz'
report='triat_bbduk.txt'
len=75

#illumina pair-end reads
/home/users/kika/bbmap/bbduk.sh overwrite=true \
	in1=$fwd in2=$rev \
	out1=$trimmed_fwd out2=$trimmed_rev \
	ref=$adapt \
	qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 minlen=$len tpe tbo t=10 2> $report
