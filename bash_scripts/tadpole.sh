#!/bin/bash

fwd_reads='/home/kika/diplonema/reads/trimmed/YPF1618_trimmed_1.fq.gz'
rev_reads='/home/kika/diplonema/reads/trimmed/YPF1618_trimmed_2.fq.gz'
reads='/home/kika/diplonema/genome_assembly/1618/tadpole/1618_extended_reads.fa'
assembly='/home/kika/diplonema/genome_assembly/1618/tadpole/1618_tadpole.fa'

/home/kika/tools/bbmap/tadpole.sh in=$reads out=$assembly k=62 threads=32
# in2=$rev_reads mode=extend 