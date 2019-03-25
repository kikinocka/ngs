#!/bin/bash

ra='/home/kika/tools/ra/build/bin/ra'
read_dir='/media/4TB1/blastocrithidia/reads/genome/'
tgs=$read_dir'pacbio/all_reads_merged.fq'
hiseq=$read_dir'trimmed/p57_all_reads_merged.fq'
assembly='/media/4TB1/blastocrithidia/genome_assembly/p57_ra/p57_ra_assembly.fa'

$ra -t 32 -x pb $tgs $hiseq > $assembly
