#!/bin/bash
#PBS -N spades
#PBS -l nodes=1:ppn=80
#PBS -l walltime=100:00:00
#PBS -m ae
#PBS -j oe

work_dir='/mnt/data/kika/blastocrithidia/b_spHR05/spades_all_careful/'
read_dir='/mnt/data/kika/blastocrithidia/b_spHR05/reads/'
fwd=$read_dir'HR05_trimmed_1.fq.gz'
rev=$read_dir'HR05_trimmed_2.fq.gz'

cd $work_dir
# spades.py --pe1-1 $fwd --pe1-2 $rev -t 40 --careful -o $work_dir
spades.py --pe1-1 $fwd --pe1-2 $rev -t 40 -o $work_dir
