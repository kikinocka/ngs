#!/bin/bash

cd '/Users/kika/ownCloud/SL_Euglenozoa/V9/above99/heterolobosea/ver2/placement/'

ssu_script='/Users/kika/scripts/py_scripts/itol_OTUs.py'
infile='heterolobosea_names.txt'

python3 $ssu_script -i $infile
