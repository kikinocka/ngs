#!/bin/bash

cd '/storage/brno12-cerit/home/kika/paratrimastix/hisat2/illumina/'

script='/storage/brno12-cerit/home/kika/scripts/py_scripts/filter_bam.py'
bam='PaPyr_ht2_sorted.bam'

python3 $script $bam
