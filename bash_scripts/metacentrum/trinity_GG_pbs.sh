#!/bin/bash
#PBS -N Trinity
#PBS -l select=1:ncpus=20:mem=30gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add trinity-2.11.0

datadir='/storage/brno3-cerit/home/kika/prototheca/wickerhamii/'
bam=$datadir'mapping/hisat2/pwic_ht2_sorted.bam'

#copy reads to scratch
cp $bam $SCRATCHDIR

report='pwic_trinity_GG.txt'


#compute on scratch
cd $SCRATCHDIR
Trinity --genome_guided_bam $bam --genome_guided_max_intron 1 --max_memory 30G --CPU $PBS_NUM_PPN 2> $report

#copy files back
rm $bam
cp -r * $datadir
