#!/bin/bash

mitofates='/mnt/mokosz/home/kika/MitoFates/MitoFates.pl'
workdir='/mnt/mokosz/home/kika/pelomyxa_schiedti/nts_charge/'
files=$workdir'*.fa'
m=metazoa
p=plant
f=fungi

cd $workdir
for file in $files; do
	echo $file
	
	out=${file%.*}'.mitofates_fungi.txt'
	perl $mitofates $file $f > $out
	
	# out=${file%.*}'.mitofates_metazoa.txt'
	# perl $mitofates $file $m > $out
done
