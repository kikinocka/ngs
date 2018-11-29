#!/bin/bash
#run on DIPLONEMA server
cd /home/tomas/GIT/busco/
export AUGUSTUS_CONFIG_PATH=/home/kika/bin/augustus-3.2.3/config/

input='/home/kika/work_dir/pelo_spades.fasta'
out='BUSCO_pelo_genome_cneo'
mode=geno
species=(cryptococcus)
lineage='/home/tomas/GIT/busco/eukaryota_odb9/'
threads=16

python BUSCO.py -i $input -m $mode -o $out -l $lineage -sp $species -c $threads --long -f
