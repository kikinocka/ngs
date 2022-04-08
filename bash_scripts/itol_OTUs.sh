#!/bin/bash

cd '/Users/kika/ownCloud/SL_Euglenozoa/V9/above99_decontaminated/stramenopiles/placement/'

ssu_script='/Users/kika/scripts/py_scripts/itol_OTUs.py'
infile='stramenopiles_names.txt'

python3 $ssu_script -i $infile
