#!/bin/bash
#PBS -N samtools_view
#PBS -l select=1:ncpus=5:mem=50gb:scratch_local=150gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add samtools-1.11

mapping_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/bw2_mapping/eukaryotes_prokka/'

#copy files to scratch
cp $mapping_dir'bml_euk_prokka_bw2_sorted.bam' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
base='bml_euk_prokka_bw2'
all=$base'_sorted.bam'
mapped=$base'_mapped_sorted.bam'

samtools view -b -F 4 $all > $mapped -@ $PBS_NUM_PPN
samtools index $mapped


#copy files back
rm $all
cp * $mapping_dir
