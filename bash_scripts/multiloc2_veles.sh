#!/bin/bash

multiloc='/home/kika/tools/MultiLoc2/src/multiloc2_prediction.py'
work_dir='/mnt/mokosz/home/kika/workdir/'
fa=$work_dir'skompletovane.fa'
r=$work_dir'skompletovane.multiloc_animal.txt'
a=animal
p=plant
f=fungal

python2.7 $multiloc -fasta=$fa -origin=$a -predictor=LowRes -result=$r -output=simple
