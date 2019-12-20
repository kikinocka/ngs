#!/bin/sh

workdir='/home/users/kika/p57/'
bam=$workdir'p57_pilon5_bw2_sorted.bam'
threads=10
output=2

cd $workdir
telomerecat bam2telbam -p $threads -v $output $bam
