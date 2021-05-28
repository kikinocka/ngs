#!/bin/bash

reads='/mnt/mokosz/home/kika/rhizomastix_vacuolata/reads/'
fwd1=$reads'RV1_trimmed_1.fq.gz'
rev1=$reads'RV1_trimmed_2.fq.gz'
fwd2=$reads'RV2_trimmed_1.fq.gz'
rev2=$reads'RV2_trimmed_2.fq.gz'

cd '/mnt/mokosz/home/kika/rhizomastix_vacuolata/'
Trinity --seqType fq --left $fwd1,$fwd2 --right $rev1,$rev2 --max_memory 100 --CPU 15
