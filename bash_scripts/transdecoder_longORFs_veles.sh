#!/bin/bash

workdir='/mnt/mokosz/home/kika/mastigella_eilhardi_MAST/'
fasta='Trinity_Mastigella_150316_renamed_nucl.fasta'

cd $workdir
TransDecoder.LongOrfs -t $fasta

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py TransDecoder done
