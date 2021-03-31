#!/bin/bash
#PBS -N quast
#PBS -l select=1:ncpus=10:mem=3gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add quast-4.6.3

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/'

#copy files to scratch
cp $datadir'spades_assembly/scaffolds.fasta' $SCRATCHDIR
cp $datadir'' $SCRATCHDIR

assemblies='scaffolds.fasta'
bam=''

#compute on scratch
cd $SCRATCHDIR
metaquast.py -o $SCRATCHDIR -t $PBS_NUM_PPN --bam $bam $assemblies


#copy results to your folder
rm $assemblies
cp -r * $datadir'quast/'
