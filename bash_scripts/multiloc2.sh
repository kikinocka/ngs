#!/bin/bash

work_dir='/home/kika/ownCloud/pelomyxa/mito_proteins/transport/tom-tim/'
fa=$work_dir'pelo_tom40_variants.fa'
r=$work_dir'pelo_tom40_variants_multiloc.txt'
a=animal
p=plant
f=fungal

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$fa -origin=$a -predictor=LowRes -result=$r -output=simple
