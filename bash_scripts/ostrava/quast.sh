#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N quast
#PBS -l nodes=1:ppn=20
#PBS -l walltime=02:00:00


assembly='/mnt/data/kika/blastocrithidia/b_spHR05/o_eliasi/Oeli.platanus_rnd2_scaffold.l500.gapcloser.fa'
out='/mnt/data/kika/blastocrithidia/b_spHR05/o_eliasi/quast/'

quast.py -o $out -t 20 $assembly
