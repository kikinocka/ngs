#!/bin/bash

fw='/media/4TB1/blastocrithidia/reads/genome/trimmed/p57_trimmed_1.fq'
rv='/media/4TB1/blastocrithidia/reads/genome/trimmed/p57_trimmed_2.fq'
out='/media/4TB1/blastocrithidia/reads/genome/trimmed/p57_read_lengths'

/home/kika/tools/bbmap/readlength.sh in=$fw in2=$rv out=$out
