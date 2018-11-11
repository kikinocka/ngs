#!/bin/bash

read_dir='/media/4TB1/diplonema/reads/genome/used/'
name='YPF1608_'
merged=$read_dir$name'merged.fq'
deduplicated=$read_dir$name'merged_deduplicated.fq'
report=$read_dir$name'report_dedupe.txt'

/home/kika/tools/bbmap/dedupe.sh in=$merged out=$deduplicated k=31 ac=f 2> $report
