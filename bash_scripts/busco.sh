#!/bin/bash
#run on DIPLONEMA server
cd /home/tomas/GIT/busco/

input='/home/kika/work_dir/pelo_schiedti_trinity.fasta'
out='BUSCO_pelo_trinity_euk'
mode=prot
species=chlamydomonas_reinhardtii
lineage='/home/tomas/GIT/busco/eukaryota_odb9/'
threads=16

python BUSCO.py -i $input -m $mode -o $out -l $lineage -c $threads --long -f
#-sp $species 