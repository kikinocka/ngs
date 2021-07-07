#!/bin/bash

qualimap='/mnt/mokosz/home/kika/tools/qualimap_v2.2.1/qualimap'
bam='/mnt/mokosz/home/kika/endolimax_nana/mapping/endo2/endo2_bw2_sorted.bam'
outdir='/mnt/mokosz/home/kika/endolimax_nana/qualimap/'
out='endo2_qualimap.pdf'
cpu=10

$qualimap bamqc -nt $cpu -bam $bam -outdir $outdir -outfile $out -outformat pdf
