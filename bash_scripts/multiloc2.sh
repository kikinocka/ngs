#!/bin/bash

work_dir='/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/fes_cluster_assembly/cia/'
fa=$work_dir'pelo_cia_aa.fa'
r=$work_dir'pelo_cia_multiloc_fungal.tsv'
a=animal
p=plant
f=fungal

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$fa -origin=$f -predictor=LowRes -result=$r -output=simple
