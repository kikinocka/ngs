#!/bin/bash
#run on DIPLONEMA server
cd /home/tomas/GIT/busco/
export AUGUSTUS_CONFIG_PATH=/home/kika/bin/augustus-3.2.3/config/

input='/home/kika/work_dir/pelomyxa_transcriptome_clean.fa'
out='BUSCO_pelo_transcriptome_clean'
mode=tran
species=(cryptococcus)
lineage='/home/tomas/GIT/busco/eukaryota_odb9/'
threads=16

python BUSCO.py -i $input -m $mode -o $out -l $lineage -c $threads --long -f
#-sp $species 
