#!/bin/bash

file_dir='/media/4TB1/diplonema/mapping/DNA_to_contigs/1621/'
reference=$file_dir'1621_modules.fa'
input=$file_dir'1621_modules_geneious.sam'
output=$file_dir'1610_geneious_stat.tsv'

/home/kika/tools/bbmap/pileup.sh in=$input out=$output ref=$reference
