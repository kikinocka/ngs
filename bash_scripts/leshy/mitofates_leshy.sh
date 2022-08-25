#!/bin/bash

mitofates='/mnt/mokosz/home/kika/MitoFates/MitoFates.pl'

cd '/mnt/mokosz/home/kika/ribosomal_proteins/'

m=metazoa
p=plant
f=fungi

for file in *.fa; do
	echo $file
	
	out=${file%.*}'.mitofates_fungi.txt'
	perl $mitofates $file $f > $out
	
	out=${file%.*}'.mitofates_metazoa.txt'
	perl $mitofates $file $m > $out
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MitoFates done
