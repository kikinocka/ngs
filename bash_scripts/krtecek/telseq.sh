#!/bin/sh

workdir='/home/users/kika/p57/'
bam=$workdir'p57_pilon5_bw2_sorted.bam'
out=$workdir'telseq/'
pattern='TTAGGG'

telseq -z $pattern -o $out $bam
