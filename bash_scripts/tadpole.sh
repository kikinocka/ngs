#!/bin/bash

fwd_reads='/home/kika/diplonema/reads/genome/trimmed/YPF1621_trimmed_1.fq.gz'
rev_reads='/home/kika/diplonema/reads/genome/trimmed/YPF1621_trimmed_2.fq.gz'
reads='/home/kika/diplonema/genome_assembly/1621/tadpole/1621_extended_reads.fa'
assembly='/home/kika/diplonema/genome_assembly/1621/tadpole/1621_tadpole.fa'

/home/kika/tools/bbmap/tadpole.sh in=$reads out=$assembly k=62 threads=32
# in=$fwd_reads in2=$rev_reads mode=extend 