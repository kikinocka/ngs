#!/bin/bash

fwd_reads='/home/kika/diplonema/reads/trimmed/YPF1601_trimmed_1.fq.gz'
rev_reads='/home/kika/diplonema/reads/trimmed/YPF1601_trimmed_2.fq.gz'
assembly='/home/kika/diplonema/genome_assembly/1601/tadpole/1601_contigs.fa'

/home/kika/tools/bbmap/tadpole.sh in=$fwd_reads in2=$rev_reads out=$assembly mode=extend k=62 threads=32