#!/bin/bash
#PBS -N TransDecoder_longORFs
#PBS -l select=1:ncpus=1:mem=2gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add transdecoder-3.0.1

data_dir='/storage/brno3-cerit/home/kika/elonga/'

#copy files to scratch
cp $data_dir'el_merged.fasta' $SCRATCHDIR

transcriptome='el_merged.fasta'

#compute on scratch
cd $SCRATCHDIR
TransDecoder.LongOrfs -t $transcriptome

#copy files back
rm $transcriptome
cp -r * $data_dir
