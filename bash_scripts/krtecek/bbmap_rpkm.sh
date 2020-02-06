#!/bin/sh

cd /home/users/kika/diplonema/

assembly='dpap_transcripts.fa'
fw=
rv=
sam='dpap_rich_bbmap_rna.sam'
rpkm='dpap_rich_bbmap.rpkm'
report='dpap_rich_bbmap.report'

bbmap.sh in=$fw in2=$rv out=$sam ref=$assembly rpkm=$rpkm threads=10 2> $report
