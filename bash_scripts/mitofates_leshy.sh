#!/bin/bash

mitofates='/mnt/mokosz/home/kika/MitoFates/MitoFates.pl'
workdir='/mnt/mokosz/home/zoli/localize/'
files=$workdir'*.fa'
m=matazoa
p=plant
f=fungi

cd $workdir
for file in $files; do
	echo $file
	
	out=${file%.*}'.mitofates_fungal.txt'
	perl $mitofates $file $f > $out
	
	# out=${file%.*}'.multiloc_animal.txt'
	# python $multiloc -fasta=$file -origin=$a -predictor=LowRes -result=$out -output=simple
done
