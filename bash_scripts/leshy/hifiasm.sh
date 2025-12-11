#!/bin/sh

cd '/mnt/mokosz/home/kika/egracilis/PacBio/'

hiafiasm='/mnt/mokosz/home/kika/tools/hifiasm/hifiasm'
reads='hifi_reads/EG_hifi.fastq.gz'

$hiafiasm -o EG_hifi.asm -t 30 $reads

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py hiafiasm done
