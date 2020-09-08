#!/bin/bash
#PBS -N telseq
#PBS -l select=1:ncpus=1:mem=10gb:scratch_local=20gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add telseq-0.0.2

datadir='/storage/brno3-cerit/home/kika/kinetoplastids/cfas_genome/'

#copy files to scratch
cp $datadir'bw2_mapping/cfas_bw2_sorted.bam' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

bam='cfas_bw2_sorted.bam'
out='cfas_telseq.out'
pattern='TTAGGG'

telseq -z $pattern -o $out $bam

#copy files back
rm $bam
cp -r * $datadir
