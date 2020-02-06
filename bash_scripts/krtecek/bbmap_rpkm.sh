#!/bin/sh

cd /home/users/kika/diplonema/

assembly='dpap_transcripts.fa'
fw='/home/users/kika/diplonema/reads_trimmed/d5_r1.fq.gz'
rv='/home/users/kika/diplonema/reads_trimmed/d5_r2.fq.gz'
sam='dpap_poor_bbmap_rna.sam'
rpkm='dpap_poor_bbmap.rpkm'
report='dpap_poor_bbmap.report'

bbmap.sh in=$fw in2=$rv out=$sam ref=$assembly rpkm=$rpkm threads=10 2> $report
