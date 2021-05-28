#!/bin/sh

read_dir='/mnt/mokosz/home/kika/rhizomastix_vacuolata/reads/'
out_dir=$read_dir'fastqc/'

cd $read_dir

for reads in *fq.gz ; do
	echo 'running FastQC on ' $reads
	fastqc -t 10 -o $out_dir $reads
done

