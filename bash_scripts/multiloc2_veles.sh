#!/bin/bash

multiloc='/home/kika/tools/MultiLoc2/src/multiloc2_prediction.py'
work_dir='/home/kika/pelomyxa_schiedti/predicted_proteins/'
fa=$work_dir'myseq7000.fa'
r=$work_dir'myseq7000.multiloc_animal.txt'
a=animal
p=plant
f=fungal

python2.7 $multiloc -fasta=$fa -origin=$a -predictor=LowRes -result=$r -output=simple
