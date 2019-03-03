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

genome_dir='/auto/brno3-cerit/nfs4/home/kika/pelomyxa/genome_assembly/'

#copy file to scratch
cd $genome_dir
cp pelomyxa_final_genome.fa $SCRATCHDIR

genome='pelomyxa_final_genome.fa'

cd $SCRATCHDIR
cegma -o pelo_p-rna-scaffolder -T $PBS_NUM_PPN -g $genome

cp pelo_p-rna-scaffolder* $genome_dir'/clean_merged_hisat2_p-rna-scaffolder/'
