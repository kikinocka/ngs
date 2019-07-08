#!/bin/bash

usearch='/home/kika/programs/usearch'

data_dir='/home/kika/ownCloud/pelomyxa_schiedti/transcriptome_assembly/'
infile=$data_dir'pelomyxa_transcriptome_clean.fa.transdecoder.5prime_complete.pep'
output=$data_dir'pelomyxa_transcriptome_clean.fa.transdecoder.5prime_complete.clustered.pep'

$usearch -cluster_fast $infile -id 0.95 -centroids $output -sort length
