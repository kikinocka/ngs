#!/bin/bash

cd '/mnt/mokosz/home/kika/workdir/'

plant='pl'
non_plant='non-pl'

for file in *; do
	echo $file
	# targetp -fasta $file -org $non_plant -format short
	targetp -fasta $file -org $plant -format short
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py TargetP done
