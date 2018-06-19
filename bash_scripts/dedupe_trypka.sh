#!/bin/bash

read_dir='/media/4TB1/diplonema/reads/genome/merged/'
name='YPF1604_'
merged=$read_dir$name'merged.fq'
deduplicated=$read_dir$name'merged_deduplicated.fq'
report=$read_dir$name'report_dedupe.txt'

/home/kika/tools/bbmap/dedupe.sh in=$merged out=$deduplicated ac=f 2> $report