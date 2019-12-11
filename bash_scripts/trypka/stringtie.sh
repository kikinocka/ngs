#!/bin/bash

stringtie='/home/kika/tools/stringtie-1.3.5.Linux_x86_64/stringtie'
bamfile='/media/4TB1/blastocrithidia/mapping/p57_ra_bowtie2_RNA/p57_ra_RNA_bw2_sorted.bam'
out='/media/4TB1/blastocrithidia/mapping/transcript_annotation/stringtie/p57_ra/p57_ra_stringtie.gff'

$stringtie $bamfile -p 32 -o $out
