#!/bin/bash

cd '/mnt/mokosz/home/kika/endolimax_nana/'

fwd1='reads/Endo1_trimmed_1.fq.gz'
rev1='reads/Endo1_trimmed_2.fq.gz'
fwd2='reads/Endo2_trimmed_1.fq.gz'
rev2='reads/Endo2_trimmed_2.fq.gz'
fwd3='reads/Endo1-2_trimmed_1.fq.gz'
rev3='reads/Endo1-2_trimmed_2.fq.gz'

Trinity --seqType fq --left $fwd1,$fwd2,$fwd3 --right $rev1,$rev2,$rev3 --max_memory 100G --CPU 15
