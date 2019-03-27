#!/bin/bash

work_dir='/home/kika/ownCloud/pelomyxa/mito_proteins/import/tom-tim/hmm/'
fa=$work_dir'pelo_Sam50_aa.fa'
r=$work_dir'pelo_Sam50_multiloc.txt'
a=animal
p=plant
f=fungal

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$fa -origin=$a -predictor=LowRes -result=$r -output=simple
