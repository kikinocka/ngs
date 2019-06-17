#!/bin/bash
#PBS -N pasa-clean
#PBS -l select=1:ncpus=1:mem=10gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add pasa-2.3.3

#copy files to scratch
cd /storage/brno3-cerit/home/kika/pelomyxa/
cp 'transcriptome_assembly/pelomyxa_trinity.fa' $SCRATCHDIR

transcripts='pelomyxa_trinity.fa'

#run on scratch
seqclean $transcripts

#copy files back
rm $transcripts
cp -r * /storage/brno3-cerit/home/kika/pelomyxa/mapping/pasa/.
