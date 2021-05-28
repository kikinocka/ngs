#!/bin/sh

read_dir='/mnt/mokosz/home/kika/endolimax_nana/reads/'
out_dir=$read_dir'fastqc/'

cd $read_dir

for reads in *fastq.gz ; do
	echo 'running FASTQC on ' $reads
	fastqc -t 10 -o $out_dir $reads
done

