#!/bin/bash

fw='/media/4TB1/blastocrithidia/reads/genome/raw/Blastoc_spP57_1.fastq.gz'
rv='/media/4TB1/blastocrithidia/reads/genome/raw/Blastoc_spP57_2.fastq.gz'
out='/media/4TB1/blastocrithidia/reads/genome/raw/p57_raw_read_lengths.tsv'

/home/kika/tools/bbmap/readlength.sh in=$fw in2=$rv out=$out
