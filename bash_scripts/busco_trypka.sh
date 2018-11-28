#!/bin/bash

cd /home/kika/miniconda3/pkgs/busco-3.0.2-py27_8/bin/
export AUGUSTUS_CONFIG_PATH=/home/kika/miniconda3/pkgs/augustus-3.3-boost1.64_bamtools2.4.1_0/config/

input='/home/kika/work_dir/pelo_spades.fasta'
out='BUSCO_pelo_genome'
mode=geno
species=chlamydomonas_reinhardtii
lineage='/home/kika/miniconda3/pkgs/busco-3.0.2-py27_8/bin/eukaryota_odb9/'
threads=30

run_BUSCO -i $input -m $mode -o $out -l $lineage -c $threads --long -f
#-sp $species 
