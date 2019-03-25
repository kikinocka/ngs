#!/bin/bash

ra='/home/kika/tools/ra/build/bin/ra'
read_dir='/media/4TB1/blastocrithidia/reads/genome/'
tgs=$read_dir'pacbio/all_reads_merged.fq'
fw=$read_dir'trimmed/p57_trimmed_1.fq'
rv=$read_dir'trimmed/p57_trimmed_2.fq'
assembly='/media/4TB1/blastocrithidia/genome_assembly/p57_ra'

$ra -t 32 -x pb $tgs $fw $rv > $assembly
