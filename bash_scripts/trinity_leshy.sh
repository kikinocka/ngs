#!/bin/bash

#CALCULATE IN TMP DIR!!!

datadir='/mnt/mokosz/home/kika/mastigamoeba_abducta_CHOM1/'

cp $datadir'reads/'*trimmed* /tmp/kika/


cd '/tmp/kika/'

fwd1='CHOM1_trimmed_1.fq.gz'
rev1='CHOM1_trimmed_2.fq.gz'
# fwd2='RV2_trimmed_1.fq.gz'
# rev2='RV2_trimmed_2.fq.gz'
# fwd3='RV1-2_trimmed_1.fq.gz'
# rev3='RV1-2_trimmed_2.fq.gz'

Trinity --seqType fq --left $fwd1 --right $rev1 --max_memory 100G --CPU 20
# Trinity --seqType fq --left $fwd1,$fwd2,$fwd3 --right $rev1,$rev2,$rev3 --max_memory 100G --CPU 15

rm *fq.gz
mv -r * $datadir

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py Trinity done
