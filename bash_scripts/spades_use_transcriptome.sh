#!/bin/bash

pe1_1='/media/4TB1/blastocrithidia/reads/genome/trimmed/triat_trimmed_1.fq'
pe1_2='/media/4TB1/blastocrithidia/reads/genome/trimmed/triat_trimmed_2.fq'
transcriptome='/media/4TB1/blastocrithidia/transcriptome_assembly/trinity_denovo/triat_default/triat_trinity.fasta'

outdir='/media/4TB1/blastocrithidia/genome_assembly/triat_spades_transcriptome/'

report=$outdir"spades_report.txt"

/home/nenarokova/tools/SPAdes-3.10.1-Linux/bin/spades.py --pe1-1 $pe1_1 --pe1-2 $pe1_2 --untrusted-contigs $transcriptome --careful -t 30 -o $outdir 2> $report
