#!/bin/bash
#PBS -N MakeBlastDB
#PBS -l select=1:ncpus=1:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a

datadir='/storage/brno12-cerit/home/kika/anaeramoeba/RABs'

#copy files to scratch
cp $datadir'/'*.fa $SCRATCHDIR
cp $datadir'/refs/'*.fa $SCRATCHDIR


#run on scratch
cd $SCRATCHDIR

dbtype=prot

for file in *.fa; do
	echo $file
	makeblastdb -in $file -dbtype $dbtype -parse_seqids
	echo *** BLASTable database done ***
done

#copy files back
rm *.fa
cp -r * $datadir'/dbs/'
