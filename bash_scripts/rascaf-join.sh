#!/bin/bash
#PBS -N rascaf-join
#PBS -l select=1:ncpus=1:mem=10gb:scratch_local=50gb
#PBS -l walltime=2:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#copy files to scratch
cd /storage/brno3-cerit/home/kika/pelomyxa/mapping/
cp pelo_clean_rascaf.out $SCRATCHDIR

cd /storage/brno2/home/kika/tools/
cp -r rascaf/ $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

rascaf_join='rascaf/rascaf-join'
rascaf_out='pelo_clean_rascaf.out'
base_name='pelo_clean_rascaf_scaffolds'

$rascaf_join -r $rascaf_out -o $base_name -ms 5

#copy files back
cp pelo_clean_rascaf_scaffolds* /storage/brno3-cerit/home/kika/pelomyxa/mapping/.
