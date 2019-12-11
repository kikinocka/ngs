#!/bin/bash

read_dir='/home/kika/diplonema/reads/merged_qtrimmed_strict/'
merged=$read_dir'YPF1604_adapter_trimmed_merged.fq'
fw=$read_dir'YPF1604_unmerged_fully_trimmed_1.fq'
rv=$read_dir'YPF1604_unmerged_fully_trimmed_2.fq'

outdir='/home/kika/diplonema/genome_assembly/1604/'
report=$outdir"spades_report.txt"

/home/kika/tools/SPAdes-3.11.1-Linux/bin/spades.py --s1 $merged --pe1-1 $fw --pe1-2 $rv --careful -m 100 -t 30 -o $outdir 2> $report
