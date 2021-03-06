#!/bin/bash

read_dir='/media/4TB1/diplonema/reads/genome/used/1610/'
reads=$read_dir'1610_D03_used_reads.fastq'

name='1610_D03_'
merged=$read_dir$name'merged.fq'
unmerged=$read_dir$name'unmerged.fq'
report=$read_dir$name'report_bbmerge.txt'
ihist=$read_dir$name'hist.txt'

/home/kika/tools/bbmap/bbmerge-auto.sh in=$reads out=$merged outu=$unmerged ihist=$ihist rem k=62 extend2=50 ecct 2> $report
