#!/bin/bash

cd '/mnt/mokosz/home/kika/archam_trees/mrbayes/'

for aln in *.nex; do
	echo $aln
	mpirun -np 4 mb -i $aln
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MrBayes done
