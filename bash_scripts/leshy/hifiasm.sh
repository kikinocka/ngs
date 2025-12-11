#!/bin/sh

cd '/mnt/mokosz/home/kika/egracilis/PacBio/'

hifiasm='/mnt/mokosz/home/kika/tools/hifiasm/hifiasm'
reads='hifi_reads/EG_hifi.fastq.gz'
name='EG_hifi.asm'

$hifiasm -o $name -t 30 $reads 2> $name.log
awk '/^S/{print ">"$2;print $3}' $name.bp.p_ctg.gfa > $name.p_ctg.fa

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py hifiasm done
