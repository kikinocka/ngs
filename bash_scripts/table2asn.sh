#!/bin/bash

table2asn='/Users/kika/programs/table2asn_GFF'

# locus_tag='Pelo'
template='/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/transcriptome/pelomyxa_template.sbt'
fasta='/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/transcriptome/pelomyxa_transcriptome_clean.for_ncbi_without_adaptors_int-ex.fa'
# gff='/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/genome/pelomyxa_prediction_final_corr.for_NCBI.gff3'
out='/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/transcriptome/pelomyxa_out.sqn'
log='/Users/kika/ownCloud/pelomyxa_schiedti/ncbi_submission/transcriptome/pelomyxa_out.log'

# #genome
# $table2asn -M n -J -c w -euk \
# 	-j "[organism=Pelomyxa schiedti] [strain=SKARADSKE] [gcode=1]" \
# 	-gaps-min 10 \
# 	-l paired-ends \
# 	-t $template \
# 	-i $fasta \
# 	-f $gff \
# 	-o $out \
# 	-Z \
# 	2> $log


#transcriptome
$table2asn -M t -J -c w -euk \
	-j "[organism=Pelomyxa schiedti] [strain=SKARADSKE] [gcode=1] [tech=TSA] [moltype=transcribed_RNA]" \
	-t $template \
	-i $fasta \
	-o $out \
	-Z \
	2> $log
