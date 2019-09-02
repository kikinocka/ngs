#!/bin/bash

usearch='/home/kika/programs/usearch'

data_dir='/home/kika/MEGAsync/diplonema/mt_metabolism/tca_cycle/KGDC_tree/'
infile=$data_dir'kgdc_deduplicated.fa'
output=$data_dir'kgdc_deduplicated.clustered.fa'

$usearch -cluster_fast $infile -id 0.7 -centroids $output -sort length
