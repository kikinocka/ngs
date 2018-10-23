#!/bin/bash

seqfire='/home/kika/programs/seqFIRE/seqfire.py'

data_dir='/home/kika/ownCloud/blastocrithidia/orthofinder/sg_ogs/jac_renamed/'
msa=$data_dir'OG0002170_renamed.aln'
out_dir=$data_dir'seqfire/'

python2 $seqfire -i $msa -a 1 -b 1 -p False 

mv *.indel *.txt *.nex $out_dir
