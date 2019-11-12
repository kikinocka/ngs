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

assembly_dir='/storage/brno3-cerit/home/kika/sags/reassembly/spades/'
cegma_dir='/storage/brno3-cerit/home/kika/sags/reassembly/reports/cegma/'

#copy file to scratch
cp $data_dir'contigs.fasta' $SCRATCHDIR

genome='contigs.fasta'
base='EU1718'

#compute on scratch
cd $SCRATCHDIR
cegma -o $base -T $PBS_NUM_PPN -g $genome

#copy files back
rm $genome
cp * $cegma_dir
