#!/bin/sh

read_dir='//mnt/mokosz/home/kika/rhizomastix_vacuolata/reads/'
out_dir='//mnt/mokosz/home/kika/rhizomastix_vacuolata/reads/fastqc/'

cd $read_dir

for reads in *fastq.gz ; do
	echo 'running FASTQC on ' $reads
	fastqc -t 10 -o $out_dir $reads
done

