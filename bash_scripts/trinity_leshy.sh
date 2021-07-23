#!/bin/bash

#CALCULATE IN TMP DIR!!!

datadir='/mnt/mokosz/home/kika/endolimax_nana'

cp $datadir'reads/'*_trimmed* /tmp/kika/


cd '/tmp/kika/'

fwd1='Endo1_trimmed_1.fq.gz'
rev1='Endo1_trimmed_2.fq.gz'
fwd2='Endo2_trimmed_1.fq.gz'
rev2='Endo2_trimmed_2.fq.gz'
fwd3='Endo1-2_trimmed_1.fq.gz'
rev3='Endo1-2_trimmed_2.fq.gz'

Trinity --seqType fq --left $fwd1,$fwd2,$fwd3 --right $rev1,$rev2,$rev3 --max_memory 100G --CPU 15

rm *fq.gz
mv -R * $datadir
