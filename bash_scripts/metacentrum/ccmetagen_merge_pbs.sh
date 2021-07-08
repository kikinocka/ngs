#!/bin/bash


module add ccmetagen-1.2.5

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/kma-ccmeta/'

# $datadir must contain .res.csv file with CCMetagen results !

level='Superkingdom'
lineage='Bacteria,Viruses'
out=$datadir'eukaryotes'

CCMetagen_merge.py -i $datadir -kr r -l $level -tlist $lineage -o $out
# -kr 
# 	k = keep
# 	r = remove
