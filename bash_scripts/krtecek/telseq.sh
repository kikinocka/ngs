#!/bin/sh

workdir='/home/users/kika/telseq/cfas/'
bam=$workdir'cfas_bw2_sorted.bam'
out=$workdir'telseq.out'
pattern='TTAGGG'

telseq -z $pattern -o $out $bam
