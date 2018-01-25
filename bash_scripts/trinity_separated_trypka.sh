#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/kika_workdir/ena_reads/'
fw=$read_dir'SRR4017973_trimmed_1.fq.gz',$read_dir'SRR4017993_trimmed_1.fq.gz'
rv=$read_dir'SRR4017973_trimmed_2.fq.gz',$read_dir'SRR4017993_trimmed_2.fq.gz'
out_dir='/media/4TB1/blastocrithidia/kika_workdir/ena_trinity/'

Trinity --seqType fq --left $fw --right $rv --output $out_dir --max_memory 100G --CPU 16

