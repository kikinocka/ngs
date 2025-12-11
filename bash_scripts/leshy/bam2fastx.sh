#!/bin/bash

cd '/mnt/mokosz/home/kika/egracilis/PacBio/hifi_reads/'

# bam2fasta='/mnt/mokosz/home/kika/miniconda3/bin/bam2fasta'
bam2fastq='/mnt/mokosz/home/kika/miniconda3/bin/bam2fastq'
bamfile='m21121_251126_103750.hifi_reads.bam'
out_prefix='EG_hifi'

# #generates <out_prefix>.fasta.gz
# $bam2fasta --num-threads 20 -o $out_prefix $bamfile

#generates <out_prefix>.fastq.gz
$bam2fastq --num-threads 20 -o $out_prefix $bamfile

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py bam2fasta done
