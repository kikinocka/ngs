#!/bin/bash

cd '/mnt/mokosz/home/kika/ribosomal_proteins/'

plant='pl'
non_plant='non-pl'

for file in *.fa; do
	echo $file
	targetp -fasta $file -org $non_plant -format short
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py TargetP done
