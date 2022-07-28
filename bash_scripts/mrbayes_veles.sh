#!/bin/bash

cd '/mnt/mokosz/home/kika/archam_trees/'

aln='hydA.trimal_gt-0.8.nex'
mpirun -np 4 mb -i $aln

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py MrBayes done
