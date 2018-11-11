#!/bin/bash

read_dir='/media/4TB1/diplonema/reads/genome/used/'
reads=$read_dir'YPF1608_used_reads.fastq'

name='YPF1608_'
merged=$read_dir$name'merged.fq'
unmerged=$read_dir$name'unmerged.fq'
report=$read_dir$name'report_bbmerge.txt'
ihist=$read_dir$name'hist.txt'

/home/kika/tools/bbmap/bbmerge-auto.sh in=$reads out=$merged outu=$unmerged ihist=$ihist rem k=62 extend2=50 ecct 2> $report
