#!/bin/sh
#PBS -N orthofinder
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=20gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add orthofinder-2.0.0

data='/storage/brno3-cerit/home/kika/archamoebae/orthofinder'

#copy files to scratch
cp $data'/'*faa $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

orthofinder -f $SCRATCHDIR -t $PBS_NUM_PPN -I 2.5

#copy files back
rm *.faa
cp -R * $data
