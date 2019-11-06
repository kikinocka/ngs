#!/bin/bash

bbmap='/home/kika/tools/bbmap/bbmap.sh'
read_dir='/media/4TB1/novymonas/transcriptome/reads/trimmed_reads/'
fw=$read_dir'wt_rna_trimmed_1.fq.gz'
rv=$read_dir'wt_rna_trimmed_2.fq.gz'
# all=$read_dir'EG_GEFR_SRR2628535.1.fq'
ref='/media/4TB1/novymonas/transcriptome/assembly/genome_based_trinity/Trinity-GG.fasta'

out_dir='/home/kika/work_dir/'
sam=$out_dir'novymonas_bb_rna.sam'
rpkm=$out_dir'novymonas_rpkm.txt'
report=$out_dir'novymonas_bbmap.report'

$bbmap in=$fw in2=$rv out=$sam ref=$ref rpkm=$rpkm threads=20 2> $report
# $bbmap in=$all out=$sam ref=$ref rpkm=$rpkm threads=30 2> $report
