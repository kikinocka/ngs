#!/bin/bash

file_dir='/media/4TB1/diplonema/mapping/DNA_to_contigs/1601/'
reference=$file_dir'1601_arrays_rest.fasta'
input=$file_dir'1601_rest_bw2.sam'
output=$file_dir'1601_rest_bw2_stat.tsv'

/home/kika/tools/bbmap/pileup.sh in=$input out=$output ref=$reference
