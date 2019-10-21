#!/bin/sh
#PBS -N Diamond-bp
#PBS -l select=1:ncpus=5:mem=20gb:scratch_local=10gb
#PBS -l walltime=01:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add diamond-0.8.29

datadir='/storage/brno3-cerit/home/kika/dmnd/'

#copy files to scratch
cp $datadir'excavata.fasta' $SCRATCHDIR

fasta='excavata.fasta'
db='excavata.dmnd'

#compute on scratch
cd $SCRATCHDIR
diamond makedb --in $fasta --db $db

#copy files back
rm $fasta
cp $db $datadir
