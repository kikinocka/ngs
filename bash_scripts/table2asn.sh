#!/bin/bash

table2asn='/mnt/mokosz/home/sebastian/linux64.table2asn_GFF'

cd '/mnt/mokosz/home/kika/pelomyxa_schiedti/ncbi_submission/'
# locus_tag='Pelo'
fasta='pelomyxa_final_corr_genome.fa'
gff='pelomyxa_prediction_final_corr.for_NCBI.gff3'
out='pelomyxa_out.sqn'
log='pelomyxa_out.log'

$table2asn -J -c w -euk \
	-j "[organism=Pelomyxa schiedti] [strain=SKARADSKE]" \
	-i $fasta \
	-f $gff \
	-o $out \
	-Z \
	2> $log

	# -locus-tag-prefix $locus_tag \