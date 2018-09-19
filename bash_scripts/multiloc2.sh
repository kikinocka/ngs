#!/bin/sh

work_dir='/home/kika/MEGAsync/blasto_project/genes/c_deaminase/possible_cd5/'
f=$work_dir'Tb927.11.16940.fa'
r=$work_dir'Tb927.11.16940_multiloc.tsv'
a=animal
p=plant
f=fungal

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$f -origin=$a -predictor=LowRes -result=$r -output=simple
