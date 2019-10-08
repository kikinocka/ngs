#!/bin/bash

pasa_path='/opt/pasa/current/scripts/'
genome='/home/kika/pelomyxa_schiedti/genome_assembly/pelomyxa_final_genome.fa'
transcriptome='/home/kika/pelomyxa_schiedti/transcriptome_assembly/pelomyxa_transcriptome_clean.fa'
evm='/home/kika/pelomyxa_schiedti/pasa-evm/evm1/evm.all.gff3'
config='pasa.annotationCompare.Template.txt'

$pasa_path'Launch_PASA_pipeline.pl' -c $config -g $genome -t $transcriptome -A -L --annots_gff3 $evm --CPU 15
$pasa_path'Launch_PASA_pipeline.pl' -c $config -g $genome -t $transcriptome -A -L \
	--annots_gff3 *.gene_structures_post_PASA_updates.*.gff3 --CPU 15

# #RUN NEXT:
# change EVM to MVE in second column
# sed 's/EVM/MVE/' 'PASA file' > updated.gff
# change . to PASA in second column
# sed 's/\(scaffold[0-9]*_[0-9]*\t\)\.\t/\1PASA\t/' updated.gff > updated2.gff
# remove all lines starting with #
# grep -v '#' updated2.gff > updated3.gff
