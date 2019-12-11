#!/bin/bash

read_dir='/home/kika/work_dir/'
in1=$read_dir'SRR2048652_1.fastq.gz'
in2=$read_dir'SRR2048652_2.fastq.gz'
out1=$read_dir'SRR2048652_trimmed_1.fq.gz'
out2=$read_dir'SRR2048652_trimmed_2.fq.gz'

/home/kika/tools/bbmap/bbduk.sh in1=$in1 in2=$in2 out1=$out1 out2=$out2 qtrim=r trimq=20 overwrite=true t=30
