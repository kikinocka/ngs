#!/bin/bash

multiloc='/opt/multiloc2/git/MultiLoc2/MultiLoc2/src/multiloc2_prediction.py'

cd '/mnt/mokosz/home/kika/workdir/'

a=animal
p=plant
f=fungal

for file in *.fa; do
	echo $file
	
	out=${file%.*}'.ML2_fungal.txt'
	python2 $multiloc -fasta=$file -origin=$f -predictor=LowRes -result=$out -output=simple
	
	out=${file%.*}'.ML2_animal.txt'
	python2 $multiloc -fasta=$file -origin=$a -predictor=LowRes -result=$out -output=simple

	# out=${file%.*}'.ML2_plant.txt'
	# python2 $multiloc -fasta=$file -origin=$p -predictor=LowRes -result=$out -output=simple
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MultiLoc2 done
