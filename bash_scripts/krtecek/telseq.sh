#!/bin/sh

workdir='/home/users/kika/tbruc/'
bam=$workdir'tbruc_bw2_sorted.bam'
out=$workdir'telseq.out'
pattern='TTAGGG'

telseq -z $pattern -o $out $bam
