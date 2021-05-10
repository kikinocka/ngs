#!/bin/bash

table2asn='/Users/kika/programs/table2asn_GFF'

locus_tag='Pelo'
# organism=''
fasta='/Users/kika/ownCloud/pelomyxa_schiedti/genome_assembly/pelomyxa_final_corr_genome.fa'
gff='/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/pelomyxa_prediction_final_corr.for_NCBI.gff3'
out='/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/pelomyxa_out.sqn'
log='/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/pelomyxa_out.log'

$table2asn -J -c w -euk \
	-locus-tag-prefix $locus_tag \
	-j "[organism=Pelomyxa schiedti] [strain=SKARADSKE]" \
	-i $fasta \
	-f $gff \
	-o $out \
	-Z \
	2> $log
