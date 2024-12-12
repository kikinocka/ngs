#!/bin/bash
#PBS -N prokka
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add conda-modules-py37

data='/storage/brno12-cerit/home/kika/kinetoplastids/strigomonadinae/'

#copy files to scratch
cp $data'K_sorsogonicus_MF08_02_endosymbiont_seprated.fasta' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
conda activate prokka 

for genome in *.fasta; do
	echo $genome
	prokka --addgenes --addmrna --cpus $PBS_NUM_PPN $genome 
done


#copy files back
rm $genome
cp -r * $data
