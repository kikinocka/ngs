#!/bin/bash
#PBS -N CCM-merge
#PBS -l select=1:ncpus=20:mem=1gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add ccmetagen-1.2.5

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/kma-ccmeta/'

#compute on scratch
cd $SCRATCHDIR

level='Kingdom'
lineage='Bacteria'
out='eukaryotes.table'

CCMetagen_merge.py -i $datadir -kr r -l $level -tlist $lineage -o $out

#copy files back
cp -R * $datadir
