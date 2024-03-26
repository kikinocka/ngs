#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N fastqc
#PBS -l nodes=1:ppn=5
#PBS -l walltime=02:00:00


read_dir='/home/users/kika/schizosaccharomyces_japonicus/reads/'
out_dir=$read_dir'fastqc/'

cd $read_dir

for reads in *.gz ; do
	echo 'running FastQC on ' $reads
	fastqc -t 5 -o $out_dir $reads
done


python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: FASTQC done
