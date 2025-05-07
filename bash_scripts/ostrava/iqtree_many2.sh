#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N IQT-many2
#PBS -l nodes=1:ppn=15
#PBS -l walltime=900:00:00


cd '/home/users/kika/iqtree/'

for f in *.aln ; do
	echo ${f}
	bb=1000
	nm=10000
	iqtree2 -m LG+C20+G4 -T 15 -B $bb --nmax $nm --quiet --safe -s ${f} --boot-trees
done

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: IQ-TREE done
