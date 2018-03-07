#!/bin/sh

f="/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/sec/el_secY_marek_without_sp.txt"
r="/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/sec/el_secY_marek_without_sp_multiloc.txt"
a=animal
p=plant

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$f -predictor=LowRes -origin=$p -result=$r -output=simple
