#!/bin/bash

workdir='/mnt/mokosz/home/kika/mastigella_eilhardi_MAST/mei_trinity_NT/'
fasta='mei.trinity.NTfilt.fasta'

cd $workdir
TransDecoder.LongOrfs -t $fasta

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py TransDecoder done
