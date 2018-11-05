#!/bin/bash
#PBS -N CEGMA
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=100gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add cegma-2.5
module add blast+-2.2.29

transc_dir='/auto/brno3-cerit/nfs4/home/kika/pelomyxa/transcriptome_assembly/pelo_all_trinity/'

#copy file to scratch
cd $transc_dir
cp Trinity.fasta $SCRATCHDIR

transcriptome='Trinity.fasta'

cd $SCRATCHDIR
cegma -o pelo_cegma -T $PBS_NUM_PPN -g $transcriptome

cp pelo_cegma $transc_dir
