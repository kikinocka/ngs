#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N gapclose
#PBS -l nodes=1:ppn=20
#PBS -l walltime=02:00:00

work_dir='/mnt/data/kika/blastocrithidia/o_volfi/scaff_gap/'

cd $work_dir
scaffolds='Ovol.platanus_rnd2_scaffold.l500.fa'
config='Ovol.rnd2.config.file'
out='Ovol.platanus_rnd2_scaffold.l500.gapcloser.fa'
log='Ovol.platanus_rnd2_scaffold.l500.gapcloser.log'

GapCloser -b $config -a $scaffolds -o $out -t 20 2> $log

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: GapCloser done
