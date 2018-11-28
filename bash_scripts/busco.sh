#!/bin/bash
#run on DIPLONEMA server
cd /home/tomas/GIT/busco/

input='/home/kika/work_dir/pelo_spades.fasta'
out='BUSCO_pelo_genome'
mode=geno
species=chlamydomonas_reinhardtii
lineage='/home/tomas/GIT/busco/eukaryota_odb9/'
threads=16

python BUSCO.py -i $input -m $mode -o $out -l $lineage -c $threads --long -f
#-sp $species 