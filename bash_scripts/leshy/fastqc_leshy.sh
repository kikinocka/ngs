#!/bin/sh

read_dir='/mnt/mokosz/home/kika/mastigamoeba_abducta_CHOM1/reads/'
out_dir=$read_dir'fastqc/'

cd $read_dir

for reads in *.gz ; do
	echo 'running FastQC on ' $reads
	fastqc -t 10 -o $out_dir $reads
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py FASTQC done
