#!/bin/bash

cd '/mnt/mokosz/home/kika/endolimax_nana/'

fwd1='reads/RV1_trimmed_1.fq.gz'
rev1='reads/RV1_trimmed_2.fq.gz'
fwd2='reads/RV2_trimmed_1.fq.gz'
rev2='reads/RV2_trimmed_2.fq.gz'

Trinity --seqType fq --left $fwd1,$fwd2 --right $rev1,$rev2 --max_memory 100G --CPU 15
