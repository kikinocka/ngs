#!/bin/bash

bbmap='/home/kika/tools/bbmap/bbmap.sh'
read_dir='/media/4TB1/blastocrithidia/reads/transcriptome/trimmed/'
fw=$read_dir'p57_trimmed_1.fq.gz'
rv=$read_dir'p57_trimmed_2.fq.gz'
# all=$read_dir'EG_GEFR_SRR2628535.1.fq'
ref='/media/4TB1/blastocrithidia/transcriptome_assembly/trinity_genome_based/p57_trinity.fasta'

out_dir='/media/4TB1/blastocrithidia/mapping/p57_bbmap_RNA/'
sam=$out_dir'p57_bb_rna.sam'
rpkm=$out_dir'p57_rpkm.txt'
report=$out_dir'p57_bbmap.report'

$bbmap in=$fw in2=$rv out=$sam ref=$ref rpkm=$rpkm threads=20 2> $report
# $bbmap in=$all out=$sam ref=$ref rpkm=$rpkm threads=30 2> $report
