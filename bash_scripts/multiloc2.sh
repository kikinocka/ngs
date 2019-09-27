#!/bin/bash

multiloc='/home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py'
work_dir='/home/kika/MEGAsync/diplonema/catalase/apx_tree/seqs/'
fa=$work_dir'euglenids_APX.fa'
r=$work_dir'euglenids_APX.multiloc.txt'
a=animal
p=plant
f=fungal

/usr/bin/python2.7 $multiloc -fasta=$fa -origin=$p -predictor=LowRes -result=$r -output=simple
