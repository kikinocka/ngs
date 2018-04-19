#!/bin/sh

f='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Calvin_cycle/RuBisCO_assembly_proteins/el_SP_cleaved.txt'
r='/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Calvin_cycle/RuBisCO_assembly_proteins/el_SP_cleaved_multiloc.tsv'
a=animal
p=plant

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$f -origin=$p -predictor=LowRes -result=$r -output=simple
