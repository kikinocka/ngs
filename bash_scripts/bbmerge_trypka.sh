#!/bin/bash

reads='/media/4TB1/diplonema/reads/genome/trimmed/'
fw=$reads'YPF1618_trimmed_1.fq.gz'
rv=$reads'YPF1618_trimmed_2.fq.gz'

dir_merged='/media/4TB1/diplonema/reads/genome/merged/'
name='YPF1618_'
merged=$dir_merged$name'merged.fq'
unmerged_fw=$dir_merged$name'unmerged_1.fq'
unmerged_rv=$dir_merged$name'unmerged_2.fq'
report=$dir_merged$name'report_bbmerge.txt'
ihist=$dir_merged$name'hist.txt'

/home/kika/tools/bbmap/bbmerge-auto.sh in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv ihist=$ihist rem k=62 extend2=50 ecct 2> $report
