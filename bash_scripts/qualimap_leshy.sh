#!/bin/bash

qualimap='/mnt/mokosz/home/kika/tools/qualimap_v2.2.1/qualimap'
bam='/mnt/mokosz/home/kika/rhizomastix_vacuolata/mapping/rvac2/rvac2_bw2_sorted.bam'
outdir='/mnt/mokosz/home/kika/rhizomastix_vacuolata/qualimap/'
out='rvac2_qualimap.pdf'
cpu=10

$qualimap bamqc -nt $cpu -bam $bam -outdir $outdir -outfile $out -outformat pdf
