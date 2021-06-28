#!/bin/bash
#PBS -N CCM-merge
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add ccmetagen-1.2.5

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/kma-ccmeta/'

# $datadir must contain .res.csv file with CCMetagen results !

level='Kingdom'
lineage='Eukaryota'
out='eukaryotes.table'

CCMetagen_merge.py -i $datadir -kr k -l $level -tlist $lineage -o $out
