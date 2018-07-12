#!/bin/bash
#run on DIPLONEMA server

input='/home/kika/work_dir/cre_proteins.fasta'
out='/home/kika/work_dir/BUSCO_cre_protists/'
mode=prot
spieces='chlamydomonas_reinhardtii'
lineage='/home/tomas/GIT/busco/protists_ensembl/'
threads=16

python /home/tomas/GIT/busco/BUSCO.py -i $input -m $mode -o $out -sp $species -l $lineage -c $threads --long -f
