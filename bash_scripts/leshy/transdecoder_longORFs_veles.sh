#!/bin/bash

workdir='/mnt/mokosz/home/kika/mastigamoeba_abducta_CHOM1/mab_trinity_NT/'
fasta='mab.trinity.NTfilt.fasta'

cd $workdir
TransDecoder.LongOrfs -t $fasta

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py TransDecoder done
