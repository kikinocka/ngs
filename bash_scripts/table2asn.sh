#!/bin/bash

table2asn='/Users/kika/programs/table2asn_GFF'

# locus_tag='Pelo'
template='/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/pelomyxa_template.sbt'
fasta='/Users/kika/ownCloud/pelomyxa_schiedti/genome_assembly/pelomyxa_final_corr_genome.fa'
gff='/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/pelomyxa_prediction_final_corr.for_NCBI.gff3'
out='/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/pelomyxa_out.sqn'
log='/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/pelomyxa_out.log'

$table2asn -M n -J -c w -euk \
	-j "[organism=Pelomyxa schiedti] [strain=SKARADSKE] [gcode=1]" \
	-gaps-min 10 \
	-l paired-ends \
	-t $template \
	-i $fasta \
	-f $gff \
	-o $out \
	-Z \
	2> $log

	# -locus-tag-prefix $locus_tag \
