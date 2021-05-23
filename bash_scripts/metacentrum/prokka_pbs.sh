#!/bin/bash
#PBS -N prokka
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=10gb
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add conda-modules-py37

data='/storage/brno3-cerit/home/kika/oil_sands/metagenome/prokka/'

#copy files to scratch
cp $data'bml_meta.spades_def.fa' $SCRATCHDIR

genome='bml_meta.spades_def.fa'
report='prokka.report'

#compute on scratch
cd $SCRATCHDIR
conda activate prokka 

prokka $genome --cpus $PBS_NUM_PPN 2> $report

#copy files back
rm $genome
cp * $data
