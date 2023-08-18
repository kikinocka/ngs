#!/bin/sh
#PBS -N orthofinder
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=20gb
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load orthofinder

data='/storage/brno3-cerit/home/kika/blasto_comparative/'

#copy files to scratch
cp $data'orthofinder/'* $SCRATCHDIR
cp $data'proteins_blasto/'*.faa $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

orthofinder -f $SCRATCHDIR -t $PBS_NUM_PPN 
#-I 2.5

#copy files back
rm *.fa *.faa *.fasta
cp -R * $data'orthofinder/'
