#!/bin/sh

work_dir='/home/kika/MEGAsync/Manuscripts/EL_plastid/tables_predictions/'
fa=$work_dir'cysJ.fa'
r=$work_dir'cysJ_multiloc.txt'
a=animal
p=plant
f=fungal

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$fa -origin=$p -predictor=LowRes -result=$r -output=simple
