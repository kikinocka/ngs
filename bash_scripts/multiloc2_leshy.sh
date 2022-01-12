#!/bin/bash

multiloc='/opt/multiloc2/git/MultiLoc2/MultiLoc2/src/multiloc2_prediction.py'
workdir='/mnt/mokosz/home/kika/ribosomal_proteins/'
files=$workdir'*.fa'
a=animal
p=plant
f=fungal

cd $workdir
for file in $files; do
	echo $file
	
	out=${file%.*}'.multiloc_fungal.txt'
	python2 $multiloc -fasta=$file -origin=$f -predictor=LowRes -result=$out -output=simple
	
	out=${file%.*}'.multiloc_animal.txt'
	python2 $multiloc -fasta=$file -origin=$a -predictor=LowRes -result=$out -output=simple
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MultiLoc2 done
