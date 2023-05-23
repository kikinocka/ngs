#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N blast
#PBS -l nodes=1:ppn=10
#PBS -l walltime=900:00:00


python3 /home/users/kika/scripts/py_scripts/blast/blast.py

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: BLAST done
