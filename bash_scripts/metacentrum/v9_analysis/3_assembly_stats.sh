#!/bin/bash

raw='/storage/brno3-cerit/home/kika/sl_euglenozoa/raw_reads/'

cd $raw
for TARGET in *.assembled.fastq ; do
    ASSEMBLED=$(wc -l < ${TARGET})
    RAW=$(sed '/^$/d' ${TARGET/.assembled/_L001_R1_001} | wc -l)
    TRIMMED=$(tail -n 1 ${TARGET/.fastq/.log} | cut -f 2)
    awk -v after=${ASSEMBLED} \
        -v before=${RAW} \
        -v trimmed=${TRIMMED} \
        -v file=${TARGET/.assembled*/} \
        'BEGIN {printf "| %s | %s | %s | %.2f | %s | %.2f |\n", file, before / 4, after / 4, 100 * after / before, trimmed, 100 * trimmed / (after / 4)}'
done
