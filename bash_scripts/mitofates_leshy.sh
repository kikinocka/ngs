#!/bin/bash

mitofates='/mnt/mokosz/home/kika/MitoFates/MitoFates.pl'
workdir='/mnt/mokosz/home/kika/workdir/'
files=$workdir'*.fa'
m=matazoa
p=plant
f=fungi

cd $workdir
for file in $files; do
	echo $file
	
	# out=${file%.*}'.mitofates_fungal.txt'
	# perl $mitofates $file $f > $out
	
	out=${file%.*}'.multiloc_metazoa.txt'
	perl $mitofates $file $m > $out
done
