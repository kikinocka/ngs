#!/bin/bash

workdir='/mnt/mokosz/home/kika/egracilis/HBDM/'
fasta='HBDM01.1.fsa_nt'

cd $workdir
TransDecoder.LongOrfs -t $fasta

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py TransDecoder done
