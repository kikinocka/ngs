#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N gapclose
#PBS -l nodes=1:ppn=20
#PBS -l walltime=02:00:00

work_dir='/mnt/data/kika/blastocrithidia/o_modryi/scaff_gap/'

cd $work_dir
scaffolds='Omod.platanus_rnd1_scaffold.l500.fa'
config='Omod.rnd1.config.file'
out='Omod.platanus_rnd1_scaffold.l500.gapcloser.fa'
log='Omod.platanus_rnd1_scaffold.l500.gapcloser.log'

GapCloser -b $config -a $scaffolds -o $out -t 20 2> $log
