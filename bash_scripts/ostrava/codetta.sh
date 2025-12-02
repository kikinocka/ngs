#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N codetta
#PBS -l nodes=1:ppn=15
#PBS -l walltime=900:00:00

codetta='/home/users/kika/codetta/codetta.py'

cd '/home/users/kika/strigomonadinae/'
# genome='p57_polished.fa'

for genome in S*.fa ; do
	echo $genome
	python $codetta $genome
done

python /home/users/kika/scripts/py_scripts/slackbot.py OSU: Codetta done
