#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N gapclose
#PBS -l nodes=1:ppn=20
#PBS -l walltime=02:00:00

work_dir='/mnt/data/kika/blastocrithidia/b_spHR05/scaff_gap/'

cd $work_dir
scaffolds='Braa.platanus_rnd1_scaffold.l500.fa'
config='Braa.rnd1.config.file'
out='Braa.platanus_rnd1_scaffold.l500.gapcloser.fa'
log='Braa.platanus_rnd1_scaffold.l500.gapcloser.log'

GapCloser -b $config -a $scaffolds -o $out -t 20 2> $log
