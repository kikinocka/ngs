#!/bin/bash

codetta='/home/users/kika/codetta/codetta.py'

cd '/home/users/kika/strigomonadinae/'
# genome='p57_polished.fa'

for genome in *.fa ; do
	python3 $codetta $genome
done
