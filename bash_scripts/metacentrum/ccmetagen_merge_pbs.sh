#!/bin/bash


module add ccmetagen-1.2.5

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/kma-ccmeta/'

# $datadir must contain .res.csv file with CCMetagen results !

level='Superkingdom'
lineage='Bacteria'
out=$datadir'eukaryotes.table'

CCMetagen_merge.py -i $datadir -kr r -l $level -tlist $lineage -o $out
# CCMetagen_merge.py -i /storage/brno3-cerit/home/kika/oil_sands/metagenome/kma-ccmeta/ -kr k -l Superkingdom -tlist Eukaryota -o eukaryotes.table
