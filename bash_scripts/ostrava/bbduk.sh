#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N bbduk
#PBS -l nodes=1:ppn=10
#PBS -l walltime=02:00:00

bbduk='/home/users/kika/bbmap/bbduk.sh'
adapt='/home/users/kika/bbmap/resources/adapters.fa'

cd '/home/users/kika/bnon_pfr_ko/reads/'
fwd='P57_PF16_1.fastq.gz'
rev='P57_PF16_2.fastq.gz'
trimmed_fwd='bnon_PF16_KO_trimmed_1.fq.gz'
trimmed_rev='bnon_PF16_KO_trimmed_2.fq.gz'
report='ovol_bbduk.txt'
# len=50

#illumina pair-end reads
$bbduk overwrite=true \
	in1=$fwd in2=$rev \
	out1=$trimmed_fwd out2=$trimmed_rev \
	ref=$adapt \
	qtrim=rl trimq=20 ktrim=r k=22 mink=11 hdist=2 tpe tbo t=10 2> $report
# minlen=$len \

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: bbduk done
