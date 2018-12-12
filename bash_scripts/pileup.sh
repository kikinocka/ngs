#!/bin/bash

file_dir='/media/4TB1/diplonema/mapping/DNA_to_contigs/1604/'
reference=$file_dir'1604_arrays.fasta'
input=$file_dir'1604_arrays_bw2.sam'
output=$file_dir'1604_arrays_bw2_stat.tsv'

/home/kika/tools/bbmap/pileup.sh in=$input out=$output ref=$reference
