#!/bin/bash
#PBS -N maker
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add maker-2.31.10
module add augustus-3.4.0
module add exonerate-2.2.0
module load genemark-4.68
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module add snap-korf/2021-11-04-gcc-10.2.1-5kjikze
module add repeatmasker


genome_dir='/storage/brno3-cerit/home/kika/blasto_comparative/final_genomes/'
datadir='/storage/brno3-cerit/home/kika/blasto_comparative/maker'

#copy files to scratch
cp $genome_dir'Omod_genome_final_masked.fa' $SCRATCHDIR
cp -r $datadir'/'* $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

mpirun -np $PBS_NUM_PPN maker

#copy files back
rm 'Omod_genome_final_masked.fa' busco*fasta
cp -R * $datadir
