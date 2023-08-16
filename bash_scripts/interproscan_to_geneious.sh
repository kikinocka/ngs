#!/bin/bash

ipr2gen='/Users/kika/scripts/py_scripts/interproscan-gff2geneious.py'

cd '/Users/kika/ownCloud/blasto_comparative/proteins/BLASTs+bedcov/'

for gff in *.gff3; do
	echo $gff
	python3 $ipr2gen $gff
done
