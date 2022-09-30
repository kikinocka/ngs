#!/bin/bash
#PBS -N bbduk
#PBS -l nodes=1:ppn=10
#PBS -l walltime=01:00:00
#PBS -m ae
#PBS -j oe


raw_dir='/mnt/data/aalbanaz/Blastocrithidia_Obscuromonas/raw_reads/Obscuromonas_oborniki/'
fwd=$raw_dir'M09_1.fastq.gz'
rev=$raw_dir'M09_2.fastq.gz'

adapt='/home/users/kika/bbmap/resources/adapters.fa'


cd '/mnt/data/kika/blastocrithidia/o_oborniki/reads/'
trimmed_fwd='M09_trimmed_1.fq.gz'
trimmed_rev='M09_trimmed_2.fq.gz'
report='oobo_bbduk.txt'
len=75

#illumina pair-end reads
/home/users/kika/bbmap/bbduk.sh overwrite=true \
	in1=$fwd in2=$rev \
	out1=$trimmed_fwd out2=$trimmed_rev \
	ref=$adapt \
	qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=10 2> $report
	# minlen=$len 