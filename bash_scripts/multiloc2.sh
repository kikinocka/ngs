#!/bin/bash

work_dir='/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/electron_transfer/'
fa=$work_dir'pelo_MDH_aa.fa'
r=$work_dir'pelo_MDH_multiloc_fungal.txt'
a=animal
p=plant
f=fungal

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$fa -origin=$f -predictor=LowRes -result=$r -output=simple
