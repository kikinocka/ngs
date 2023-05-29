#!/bin/bash

workdir='/mnt/mokosz/home/kika/eukDB/'
fasta='Microheliella_maris.fna'

cd $workdir
TransDecoder.LongOrfs -t $fasta

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py TransDecoder done
