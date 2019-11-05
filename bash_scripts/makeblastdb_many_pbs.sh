#!/bin/bash
#PBS -N MakeBlastDB
#PBS -l select=1:ncpus=1:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.7.1

datadir='/storage/brno3-cerit/home/kika/elonga_bct_genomes/'
files=$datadir'*.fna'

for file in $files; do
	echo $file
	makeblastdb -in $file -dbtype nucl -parse_seqids
done
