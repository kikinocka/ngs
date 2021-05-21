#!/bin/bash
#PBS -N samtools_depth
#PBS -l select=1:ncpus=5:mem=50gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add samtools-1.11

mapping_dir='/storage/brno3-cerit/home/kika/pelomyxa/mapping/bowtie2/DNA_to_genome'

#copy files to scratch
cp $mapping_dir'/pelo_genome_bw2_sorted.bam' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
bam=$base'pelo_genome_bw2_sorted.bam'

samtools depth -a $bam | awk '{sum+=$3} END { print "Average = ",sum/NR}'


#copy files back
rm $bam
cp * $mapping_dir'/depth/'
