#!/bin/bash

input='/media/4TB1/diplonema/mapping/DNA_to_contigs/1608/1608_contigs_DNA_bw2.sam'
output='/media/4TB1/diplonema/mapping/DNA_to_contigs/1608/1608_contigs_DNA_bw2_stat.tsv'
transcriptome='/media/4TB1/diplonema/mapping/DNA_to_contigs/1608/1608_final_chromosomes.fasta'

/home/kika/tools/bbmap/pileup.sh in=$input out=$output ref=$transcriptome
