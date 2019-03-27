#!/bin/bash

cufflinks='/home/kika/tools/cufflinks-2.2.1.Linux_x86_64/cufflinks'
bamfile='/media/4TB1/blastocrithidia/mapping/p57_ra_bowtie2_RNA/p57_ra_RNA_bw2_sorted.bam'
outdir='/media/4TB1/blastocrithidia/mapping/transcript_annotation/cufflinks/p57_ra/'

$cufflinks -p 32 -o $outdir $bamfile