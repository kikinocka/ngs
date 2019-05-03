#!/bin/bash
#PBS -N TransDecoder
#PBS -l select=1:ncpus=1:mem=20gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add transdecoder-3.0.1

data_dir='/storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/'

#copy files to scratch
cd $data_dir
cp pelomyxa_trinity.fa $SCRATCHDIR

transcriptome='pelomyxa_trinity.fa'

#compute on scratch
cd $SCRATCHDIR
TransDecoder.LongOrfs -t $transcriptome

#copy files back
rm $transcriptome
cp -r * $data_dir'transdecoder/'
