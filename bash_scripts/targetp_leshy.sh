#!/bin/bash

workdir='/mnt/mokosz/home/kika/workdir/'
files=$workdir'*.fa'
plant='pl'
non_plant='non-pl'

cd $workdir
for file in $files; do
	echo $file
	targetp -fasta $file -org $non_plant -format short
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py TargetP done
