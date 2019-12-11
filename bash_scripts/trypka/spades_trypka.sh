#!/bin/bash

read_dir='/media/4TB1/blastocrithidia/reads/ku_mutants/'
pe1_1=$read_dir'Lmex_Ku80_trimmed_1.fq.gz'
pe1_2=$read_dir'Lmex_Ku80_trimmed_2.fq.gz'

outdir='/media/4TB1/blastocrithidia/genome_assembly/ku_mutants/Lmex_Ku80/'
report=$outdir'spades_report.txt'

/home/kika/tools/SPAdes-3.11.1-Linux/bin/spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 --careful -t 32 -o $outdir 2> $report
