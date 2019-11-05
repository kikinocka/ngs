#!/bin/bash

multiloc='/home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py'
work_dir='/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/energy_generation/'
fa=$work_dir'pelo_pfo_predicted.fa'
r=$work_dir'pelo_pfo_predicted.multiloc_fungal.txt'
a=animal
p=plant
f=fungal

/usr/bin/python2.7 $multiloc -fasta=$fa -origin=$f -predictor=LowRes -result=$r -output=simple
