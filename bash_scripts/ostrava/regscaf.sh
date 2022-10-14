#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N regscaf
#PBS -l nodes=1:ppn=40
#PBS -l walltime=24:00:00


cd '/home/users/kika/RegScaf/'
pipeline='pipeline.sh'
genome='test_data/genome.fa'
out='test_out'

sh $pipeline $genome $out
