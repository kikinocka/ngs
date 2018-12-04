#!/bin/bash

file_dir='/media/4TB1/diplonema/mapping/DNA_to_contigs/1618/'
reference=$file_dir'1618_C01_2-D02_2.fasta'
input=$file_dir'1618_C01_2-D02_2_bw2.sam'
output=$file_dir'1618_C01_2-D02_2_bw2_stat.tsv'

/home/kika/tools/bbmap/pileup.sh in=$input out=$output ref=$reference
