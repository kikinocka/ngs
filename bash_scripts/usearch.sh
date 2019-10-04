#!/bin/bash

usearch='/home/kika/programs/usearch'

data_dir='/home/kika/ownCloud/pelomyxa_schiedti/predicted_proteins/'
infile=$data_dir'pelo_transcriptome_clean.fa.transdecoder.5prime_complete.pep'
output=$data_dir'usearch_0.95.fa'

$usearch -cluster_fast $infile -id 0.95 -centroids $output -sort length
