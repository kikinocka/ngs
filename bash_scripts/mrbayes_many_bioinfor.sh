#!/bin/bash
#PBS -N mrbayes-many
#PBS -l nodes=1:ppn=4,walltime=168:00:00
#PBS -q default
#PBS -M kika.zahonova@gmail.com
#PBS -m ae
#PBS -j oe

##print Node Hostname, the time and date, handy for trouble shooting
echo $HOSTNAME
date

##run mrbayes program
cd '/home/kristinaz/trafficking/arfs/'


for aln in *.nex; do
	mpirun -np 4 mb -i $aln
done
