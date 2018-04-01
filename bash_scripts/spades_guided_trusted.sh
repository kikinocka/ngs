#!/bin/bash

pe1_1='/home/kika/diplonema/reads/trimmed/YPF1601_trimmed_1.fq.gz'
pe1_2='/home/kika/diplonema/reads/trimmed/YPF1601_trimmed_2.fq.gz'
additional='/home/kika/diplonema/genome_assembly/1601/tadpole/1601_tadpole.fa'

outdir='/home/kika/diplonema/genome_assembly/1601/spades_guided_trusted/'

report=$outdir"spades_report.txt"

/home/nenarokova/tools/SPAdes-3.10.1-Linux/bin/spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 --trusted-contigs $additional --careful -t 30 -o $outdir 2> $report
