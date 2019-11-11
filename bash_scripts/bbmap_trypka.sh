#!/bin/bash

bbmap='/home/kika/tools/bbmap/bbmap.sh'
read_dir='/home/kika/work_dir/'
fw=$read_dir'SRR2048655_trimmed_1.fq.gz'
rv=$read_dir'SRR2048655_trimmed_2.fq.gz'
# all=$read_dir'EG_GEFR_SRR2628535.1.fq'
ref='/home/kika/work_dir/TriTrypDB-46_LseymouriATCC30220_AnnotatedCDSs.fasta'

out_dir='/home/kika/work_dir/'
sam=$out_dir'lsey_35_bb_rna.sam'
rpkm=$out_dir'lsey_35_rpkm.txt'
report=$out_dir'lsey_35_bbmap.report'

$bbmap in=$fw in2=$rv out=$sam ref=$ref rpkm=$rpkm threads=30 2> $report
# $bbmap in=$all out=$sam ref=$ref rpkm=$rpkm threads=30 2> $report
