#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N Trinity
#PBS -l nodes=1:ppn=20
#PBS -l walltime=100:00:00


cd '/home/users/kika/schizosaccharomyces_japonicus/'

read_dir='reads/'
out_dir='donna1_trinity'

fw=$read_dir'NG-A0875_Donna_1_trimmed_1.fq.gz'
rv=$read_dir'NG-A0875_Donna_1_trimmed_2.fq.gz'


Trinity --seqType fq --left $fw --right $rv --output $out_dir --CPU 30

