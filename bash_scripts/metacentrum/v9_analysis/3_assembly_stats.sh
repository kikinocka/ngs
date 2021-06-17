#!/bin/bash

raw='/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/merged_pear/'
path1='/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/raw_reads/'
path2='/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/trimmed_cutadapt/'
cd $raw
for TARGET in *.assembled.fastq ; do
	cd $raw
    ASSEMBLED=$(wc -l < ${TARGET})
    cd $path1
    RAW=$(sed '/^$/d' ${TARGET/.assembled/_L001_R1_001} | wc -l)
    cd $path2
    TRIMMED=$(tail -n 1 ${TARGET/.fastq/.log} | cut -f 2)
    awk -v after=${ASSEMBLED} \
        -v before=${RAW} \
        -v trimmed=${TRIMMED} \
        -v file=${TARGET/.assembled*/} \
        'BEGIN {printf "| %s | %s | %s | %.2f | %s | %.2f |\n", file, before / 4, after / 4, 100 * after / before, trimmed, 100 * trimmed / (after / 4)}'
done
