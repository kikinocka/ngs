#!/bin/bash

input='/media/4TB1/diplonema/mapping/RNA_to_transcriptomes/1604/1604_RNA_full_bw2.sam'
output='/media/4TB1/diplonema/mapping/RNA_to_transcriptomes/1604/1604_RNA_full_bw2_stat.tsv'
transcriptome='/media/4TB1/diplonema/transcriptomes/1604_Trinity.fasta'

/home/kika/tools/bbmap/pileup.sh in=$input out=$output ref=$transcriptome
