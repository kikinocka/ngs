#!/bin/bash
#PBS -N bedtools-genomecov
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load bedtools

assembly_dir='/storage/brno3-cerit/home/kika/blasto_comparative/final_genomes/'
mapping_dir='/storage/brno3-cerit/home/kika/blasto_comparative/hisat2/btri/'


#copy files to scratch
cp $assembly_dir'Btri_genome_final_masked.fa' $SCRATCHDIR
cp $mapping_dir'btri_ht2_sorted.bam' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

genome='Btri_genome_final_masked.fa'
bamfile='btri_ht2_sorted.bam'
out='btri_genomecoverage.tsv'

bedtools genomecov -bga -split -ibam $bamfile -g $genome > $out


#copy files back
rm $genome $bamfile
cp -r * $mapping_dir
