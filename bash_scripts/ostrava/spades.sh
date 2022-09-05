#!/bin/bash
#PBS -N spades
#PBS -l nodes=1:ppn=80
#PBS -l walltime=100:00:00
#PBS -m ae
#PBS -j oe

work_dir='/mnt/data/kika/blastocrithidia/b_triatomae/spades_careful/'
read_dir='/mnt/data/kika/blastocrithidia/b_triatomae/reads/'
fwd=$read_dir'triat_trimmed_75_1.fq'
rev=$read_dir'triat_trimmed_75_2.fq'

cd $work_dir
spades.py --pe1-1 $fwd --pe1-2 $rev -t 40 --careful -o $work_dir
