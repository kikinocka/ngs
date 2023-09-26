#!/bin/sh

if_removal='/storage/brno2/home/kika/scripts/py_scripts/remove_isoforms.py'

cd '/storage/brno3-cerit/home/kika/archamoebae/prot_assemblies_filtration-20220127/'

infile='enan.trinity.NRfilt.faa'

python3 $if_removal $infile
