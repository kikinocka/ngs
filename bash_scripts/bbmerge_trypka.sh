#!/bin/bash

dir_raw='/home/kika/diplonema/reads/adapter_trimmed/'
fw=$dir_raw'YPF1604_adapter_trimmed_1.fq.gz'
rv=$dir_raw'YPF1604_adapter_trimmed_2.fq.gz'

dir_merged='/home/kika/diplonema/reads/merged_qtrimmed_ustrict/'
name='YPF1604_adapter_trimmed'
merged=$dir_merged$name'_merged.fq'
unmerged_fw=$dir_merged$name'_unmerged_1.fq'
unmerged_rv=$dir_merged$name'_unmerged_2.fq'
report=$dir_merged$name'_report.txt'
ihist=$dir_merged$name'_hist.txt'
# extra1=$dir_raw"E262_1_trimmed.fastq"
# extra2=$dir_raw"E262_2_trimmed.fastq"
# extra3=$dir_raw"wt_S2_L001_unmerged_trimmed_1.fq"
# extra4=$dir_raw"wt_S2_L001_unmerged_trimmed_2.fq"

/home/kika/tools/bbmap/bbmerge-auto.sh in1=$fw in2=$rv out=$merged outu1=$unmerged_fw outu2=$unmerged_rv ihist=$ihist ustrict=t qtrim2=t usejni=t rem extend2=50 k=62 2> $report
# extra=$extra1,$extra2,$extra3,$extra4