#!/bin/bash

input='/media/4TB1/diplonema/mapping/DNA_to_contigs/1608/1608_cassettes-arrays_bw2.sam'
output='/media/4TB1/diplonema/mapping/DNA_to_contigs/1608/1608_cassettes-arrays_bw2_stat.tsv'
reference='/media/4TB1/diplonema/mapping/DNA_to_contigs/1608/1608_cassettes-arrays.fasta'

/home/kika/tools/bbmap/pileup.sh in=$input out=$output ref=$reference
