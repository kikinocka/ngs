#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N codetta
#PBS -l nodes=1:ppn=1
#PBS -l walltime=50:00:00

cd '/home/users/kika/blastocrithidia/final_assemblies'

codetta_dir='/home/users/kika/codetta/'
codetta=$codetta_dir'codetta.py'
profiles=$codetta_dir'resources/Pfam-A_enone.hmm'
genome='/home/users/kika/blastocrithidia/final_assemblies/Braa_genome_final_masked.fa'

python3 $codetta -p $profiles $genome

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: codetta done
