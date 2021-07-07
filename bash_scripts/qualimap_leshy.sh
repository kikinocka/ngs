#!/bin/bash

qualimap='/mnt/mokosz/home/kika/tools/qualimap_v2.2.1/qualimap'
bam='/mnt/mokosz/home/kika/endolimax_nana/mapping/endo1/endo1_bw2_sorted.bam'
outdir='/mnt/mokosz/home/kika/endolimax_nana/qualimap/'
out='endo1_qualimap.pdf'
cpu=10

$qualimap bamqc -nt $cpu -bam $bam -outdir $outdir -outfile $out -outformat pdf
