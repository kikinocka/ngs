#!/bin/sh
#PBS -N bbmerge
#PBS -l select=1:ncpus=10:mem=10gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add orthofinder-2.0.0

data='/storage/brno3-cerit/home/kika/pelomyxa/peroxisomes'


#copy files to scratch
cp $data'mastig_lopit_prot.fa' $SCRATCHDIR
cp $data'pelomyxa_predicted_proteins_corr.fa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

orthofinder -f $SCRATCHDIR

#copy files back
rm 'mastig_lopit_prot.fa' 'pelomyxa_predicted_proteins_corr.fa'
cp -R * $data
