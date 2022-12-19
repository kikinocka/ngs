#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N codetta
#PBS -l nodes=1:ppn=1
#PBS -l walltime=50:00:00

cd '/home/users/kika/blastocrithidia/final_assemblies/'

codetta_dir='/home/users/kika/codetta/'
codetta=$codetta_dir'codetta.py'

python3 $codetta $genome

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: codetta done
