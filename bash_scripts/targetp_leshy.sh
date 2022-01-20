#!/bin/bash

cd '/mnt/mokosz/home/kika/replisome/'
infile='rfa2.fa'
plant='pl'
non_plant='non-pl'

targetp -fasta $infile -org $non_plant -format short

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py TargetP done
