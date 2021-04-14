#!/bin/bash

multiloc='/opt/multiloc2/git/MultiLoc2/MultiLoc2/src/multiloc2_prediction.py'
workdir='/mnt/mokosz/home/kika/workdir/'
files=$workdir'*.fasta'
a=animal
p=plant
f=fungal

cd $workdir
for file in $files; do
	echo $file
	
	out=${file%.*}'.multiloc_fungal.txt'
	python $multiloc -fasta=$file -origin=$f -predictor=LowRes -result=$out -output=simple
	
	out=${file%.*}'.multiloc_animal.txt'
	python $multiloc -fasta=$file -origin=$a -predictor=LowRes -result=$out -output=simple
done
