#!/bin/sh

genome='/Users/kika/ownCloud/pelomyxa_schiedti/genome_assembly/pelomyxa_final_corr_genome.fa'
gff='/Users/kika/ownCloud/pelomyxa_schiedti/pasa-evm/pelomyxa_prediction_final_corr.gff3'
proteins='/Users/kika/ownCloud/pelomyxa_schiedti/pasa-evm/pelomyxa_predicted_proteins_corr2.fa'

gffread $gff -g $genome -y $proteins
