#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N gapclose
#PBS -l nodes=1:ppn=20
#PBS -l walltime=100:00:00

gapcloser='/home/users/kika/gapcloser/Release/stLFR_GapCloser'
work_dir='/mnt/data/kika/blastocrithidia/b_frustrata/scaff_gap/'

cd $work_dir
scaffolds='Bfru.platanus_rnd1_scaffold.l500.fa'
out='Bfru.platanus_rnd1_scaffold.l500.gapcloser.fa'
config='config.file'

$gapcloser -b $config -a $scaffolds -o $out -t 20
