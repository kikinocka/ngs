#!/bin/bash

data='/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/'
raw=$data'raw_reads/'
merged=$data'merged_pear/'
trimmed=$data'trimmed_cutadapt/'

cd $merged
for TARGET in *.assembled.fastq ; do
	cd $merged
	echo 'I am in: ' $merged
    ASSEMBLED=$(wc -l < ${TARGET})
    echo 'Target is: ' $TARGET

    cd $raw
    echo 'I am in: ' $raw
    fwd=${TARGET/.assembled/_L001_R1_001}
    echo 'Extracting: ' $fwd.gz
    gzip -k -d $fwd.gz
    RAW=$(sed '/^$/d' $fwd | wc -l)
    echo 'Removing: ' $fwd
    rm $fwd
    
    cd $trimmed
    echo 'I am in: ' $trimmed
    TRIMMED=$(tail -n 1 ${TARGET/.fastq/.log} | cut -f 2)
    echo 'Target is: ' ${TARGET/.fastq/.log}
    
    awk -v after=${ASSEMBLED} \
        -v before=${RAW} \
        -v trimmed=${TRIMMED} \
        -v file=${TARGET/.assembled*/} \
        'BEGIN {printf "| %s | %s | %s | %.2f | %s | %.2f |\n", file, before / 4, after / 4, 100 * after / before, trimmed, 100 * trimmed / (after / 4)}'
    echo 'awk done'
    echo '**********************************'
done
