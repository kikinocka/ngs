#!/bin/bash

codetta='/home/users/kika/codetta/codetta.py'

cd '/home/users/kika/strigomonadinae/'
# genome='p57_polished.fa'

for genome in *.fa ; do
	echo $genome
	python3 $codetta $genome
done

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: Codetta done
