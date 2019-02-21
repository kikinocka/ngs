#!/bin/bash
#PBS -N rascaf
#PBS -l select=1:ncpus=1:mem=15gb:scratch_local=100gb
#PBS -l walltime=2:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#copy files to scratch
cd /storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/
cp pelomyxa_clean.fa $SCRATCHDIR

cd /storage/brno3-cerit/home/kika/pelomyxa/mapping/
cp pelo_clean_bw2_sorted.bam $SCRATCHDIR

cd /storage/brno2/home/kika/tools/
cp -r rascaf/ $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

rascaf='rascaf/rascaf'
assembly='pelomyxa_clean.fa'
bam_file='pelo_clean_bw2_sorted.bam'
base_name='pelo_clean_rascaf'

$rascaf -b $bam_file -f $assembly -o $base_name
$rascaf_join -r $base_name'.out' -o $base_name -ms 5

#copy files back
cp pelo_clean_rascaf* /storage/brno3-cerit/home/kika/pelomyxa/mapping/.
