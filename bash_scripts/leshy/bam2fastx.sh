#!/bin/bash

cd '/mnt/mokosz/home/kika/egracilis/PacBio/'

bamfile='euglena_m21121_251212_153655.hifi_reads.bc2002.bam'
out_prefix='EG_hifi'

# #generates <out_prefix>.fasta.gz
# bam2fasta --num-threads 20 -o $out_prefix $bamfile

#generates <out_prefix>.fastq.gz
bam2fastq --num-threads 20 -o $out_prefix $bamfile

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py bam2fasta/q done
