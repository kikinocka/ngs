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
mapping_dir='/storage/brno3-cerit/home/kika/blasto_comparative/hisat2/braa/final_corrected2/'


#copy files to scratch
cp $assembly_dir'Braa_genome_final_corrected2_masked.fa' $SCRATCHDIR
cp $mapping_dir'braa_ht2_sorted.bam' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

genome='Braa_genome_final_corrected2_masked.fa'
bamfile='braa_ht2_sorted.bam'
out='braa_gencov.tsv'

bedtools genomecov -bga -split -ibam $bamfile -g $genome > $out


#copy files back
rm $genome $bamfile
cp -r * '/storage/brno3-cerit/home/kika/blasto_comparative/hisat2/genome_cov/'
