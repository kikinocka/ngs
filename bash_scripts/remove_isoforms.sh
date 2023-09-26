#!/bin/sh

if_removal='/storage/brno2/home/kika/scripts/py_scripts/remove_isoforms.py'

cd '/storage/brno3-cerit/home/kika/archamoebae/prot_assemblies_filtration-20220127/'

for infile in *renamed.NRfilt.faa; do
	echo $infile
	python3 $if_removal $infile
done
