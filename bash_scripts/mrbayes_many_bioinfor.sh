#!/bin/bash
#PBS -N mrbayes-many
#PBS -l nodes=1,walltime=24:00:00
#PBS -q default
#PBS -M kika.zahonova@gmail.com
#PBS -m abe

##print Node Hostname, the time and date, handy for trouble shooting
echo $HOSTNAME
date

##run mrbayes program
cd '/home/kristinaz/trafficking/arfs/'


for aln in *.nex; do
	mb -i $aln
done
