#!/bin/bash
#PBS -N fastqc
#PBS -l nodes=1:ppn=5
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cd '/mnt/data/kika/blastocrithidia/o_oborniki/reads/'
fwd='karect_M09_trimmed_75_1.fq'
rev='karect_M09_trimmed_75_2.fq'

fastqc -o ./fastqc -t 5 $fwd $rev
