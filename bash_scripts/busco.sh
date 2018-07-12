#!/bin/bash
#run on DIPLONEMA server
cd /home/tomas/GIT/busco/

input='/home/kika/work_dir/cre_proteins.fasta'
out='BUSCO_cre_protists'
mode=prot
species=chlamydomonas_reinhardtii
lineage='/home/tomas/GIT/busco/protists_ensembl/'
threads=16

python BUSCO.py -i $input -m $mode -o $out -sp $species -l $lineage -c $threads --long -f
