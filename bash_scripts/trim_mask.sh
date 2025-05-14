#!/bin/bash

cd '/Users/kika/ownCloud/membrane-trafficking/clathrin/ASR_opisthokonta/CLC/ver2/'

trimmask='/Users/kika/scripts/py_scripts/trim_mask.py'
full_aln='CLC_opisthokonta.mafft.aln'
trim_aln='CLC_opisthokonta.man_trim.aln'

python3 $trimmask -f $full_aln -t $trim_aln

#trim_mask.py [-h] -f FULL_ALIGNMENT [-o OUTFILE] [-t TRIM_ALIGNMENT | -m MASK]