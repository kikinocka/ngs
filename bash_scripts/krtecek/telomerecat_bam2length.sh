#!/bin/sh

workdir='/home/users/kika/p57/'
bam=$workdir'p57_pilon5_bw2_sorted.bam'
output=$workdir'p57_telomeres.csv'
threads=15
out=1
# 0: No output [Default]
# 1: Total Reads Processed
# 2: Detailed output

cd $workdir
telomerecat bam2length -p $threads -v $out --output $output $bam
