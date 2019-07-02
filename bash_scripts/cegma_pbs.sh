#!/bin/bash
#PBS -N CEGMA
#PBS -l select=1:ncpus=5:mem=10gb:scratch_local=100gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add cegma-2.5
module add blast+-2.2.29

data_dir='/storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/'

#copy file to scratch
cp $data_dir'pelomyxa_transcriptome_clean.fa' $SCRATCHDIR

genome='pelomyxa_transcriptome_clean.fa'

cd $SCRATCHDIR
cegma -o pelo_clean -T $PBS_NUM_PPN -g $genome

cp pelo_clean* $data_dir'/cegma/pelo_clean/.'
