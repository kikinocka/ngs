#!/bin/bash

read_dir='/home/kika/diplonema/reads/trimmed/'
pe1_1=$read_dir'YPF1610_trimmed_1.fq.gz'
pe1_2=$read_dir'YPF1610_trimmed_2.fq.gz'

outdir='/home/kika/diplonema/genome_assembly/1610/'
report=$outdir'spades_report.txt'

/home/kika/tools/SPAdes-3.11.1-Linux/bin/spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 --careful -t 32 -o $outdir 2> $report
