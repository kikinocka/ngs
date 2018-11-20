#!/bin/bash

file_dir='/media/4TB1/diplonema/mapping/DNA_to_contigs/1618/'
reference=$file_dir'NODE_41415_length_485_cov_989.650838.fasta'
input=$file_dir'NODE_41415_bw2.sam'
output=$file_dir'NODE_41415_bw2_stat.tsv'

/home/kika/tools/bbmap/pileup.sh in=$input out=$output ref=$reference
