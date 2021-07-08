#!/bin/bash


module add ccmetagen-1.2.5

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/kma-ccmeta/'

csv=$datadir'CCMetagen.res.csv'
frag=$datadir'bml_kma.frag'
out=$datadir'eukaryotes.fa'
level='Superkingdom'
lineage='Eukaryota'

CCMetagen_extract_seqs.py -iccm $csv -ifrag $frag -l $level -t $lineage -o $out
