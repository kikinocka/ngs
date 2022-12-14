#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N quast
#PBS -l nodes=1:ppn=20
#PBS -l walltime=02:00:00

cd '/mnt/data/kika/blastocrithidia/final_assemblies/'

for assembly in *.fa; do
	out='quast/'${assembly%.fa}
	quast.py -o $out -t 20 $assembly
done

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: QUAST done
