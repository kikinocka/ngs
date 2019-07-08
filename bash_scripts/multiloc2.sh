#!/bin/bash

work_dir='/home/kika/ownCloud/pelomyxa_schiedti/predicted_proteins/'
fa=$work_dir'pelomyxa_transcriptome_clean.fa.transdecoder.5prime_complete.clustered.pep'
r=$work_dir'proteins_multiloc_fungal.txt'
a=animal
p=plant
f=fungal

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$fa -origin=$f -predictor=LowRes -result=$r -output=simple
