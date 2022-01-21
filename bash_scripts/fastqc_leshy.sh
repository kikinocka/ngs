#!/bin/sh

read_dir='/mnt/mokosz/home/kika/mastigamoeba_abducta_CHOM/reads/'
out_dir=$read_dir'fastqc/'

cd $read_dir

for reads in * ; do
	echo 'running FastQC on ' $reads
	fastqc -t 10 -o $out_dir $reads
done

