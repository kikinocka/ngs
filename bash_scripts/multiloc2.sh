#!/bin/bash

multiloc='/home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py'
work_dir='/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/tca_cycle/'
fa=$work_dir'tca_cycle.fa'
r=$work_dir'tca_cycle_multiloc_animal.txt'
a=animal
p=plant
f=fungal

/usr/bin/python2.7 $multiloc -fasta=$fa -origin=$a -predictor=LowRes -result=$r -output=simple
