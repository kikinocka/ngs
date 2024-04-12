#!/bin/bash
#PBS -N prokka
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add conda-modules-py37

data='/storage/brno3-cerit/home/kika/chloroflexi/'

#copy files to scratch
cp $data'Chloroflexi_genome_scaffolds.fa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
conda activate prokka 

genome='Chloroflexi_genome_scaffolds.fa'
prokka --addgenes --addmrna --cpus $PBS_NUM_PPN $genome 

#copy files back
rm $genome
cp -r * $data
