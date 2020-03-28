#!/bin/bash
#PBS -N MakeBlastDB
#PBS -l select=1:ncpus=1:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.7.1

datadir='/auto/brno3-cerit/nfs4/home/fussyz01/hampllab/MMETSP1310/'
files=$datadir'*.nt.fa.txt'
dbtype=nucl

for file in $files; do
	echo $file
	makeblastdb -in $file -dbtype $dbtype -parse_seqids
done
