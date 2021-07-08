#!/bin/bash

qualimap='/mnt/mokosz/home/kika/tools/qualimap_v2.2.1/qualimap'
bam='/mnt/mokosz/home/kika/rhizomastix_libera+elongata_reassembly/mapping/rlib_bw2_sorted.bam'
outdir='/mnt/mokosz/home/kika/rhizomastix_vacuolata/qualimap/'
out='rlib_qualimap.pdf'
cpu=10
mem=5G

$qualimap bamqc -nt $cpu --java-mem-size $mem -bam $bam -outdir $outdir -outfile $out -outformat pdf
