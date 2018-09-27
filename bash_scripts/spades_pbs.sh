#!/bin/bash
#PBS -N SPAdes
#PBS -l select=1:ncpus=4:mem=1tb:scratch_local=10gb
#PBS -l walltime=1:00:00

spades='/auto/brno2/home/kika/tools/SPAdes-3.11.1-Linux/bin/spades.py'

read_dir='/home/kika/diplonema/reads/trimmed/'
fwd=$read_dir'YPF1621_trimmed_1.fq.gz'
rv=$read_dir'YPF1621_trimmed_2.fq.gz'

outdir='/home/kika/diplonema/genome_assembly/1621/'
report=$outdir'spades_report.txt'

spades --pe1-1 $fwd --pe1-2 $rv --careful -t 32 -m 1000 -o $outdir 2> $report
