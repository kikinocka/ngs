#!/bin/sh

f="/home/kika/MEGAsync/Chlamydomonas/od_toma/putative_pt_genes_aa_complete5.fa"
r="/home/kika/MEGAsync/Chlamydomonas/od_toma/putative_pt_genes_aa_complete5_multiloc.txt"
a=animal
p=plant

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$f -predictor=LowRes -origin=$p -result=$r -output=simple
