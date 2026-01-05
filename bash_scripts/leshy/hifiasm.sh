#!/bin/sh

cd '/mnt/mokosz/home/kika/egracilis/PacBio/'

hifiasm='/mnt/mokosz/home/kika/tools/hifiasm/hifiasm'
reads='reads/euglena_m21121_251212_153655.hifi_reads.bc2002.filt.fastq.gz'
name='EG_hifi.asm'

$hifiasm -o $name -t 30 $reads 2> $name.log
#--telo-m CCCTAA 
awk '/^S/{print ">"$2;print $3}' $name.bp.p_ctg.gfa > $name.p_ctg.fa

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py hifiasm done
