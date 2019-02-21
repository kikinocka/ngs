#!/bin/bash
#PBS -N rascaf
#PBS -l select=1:ncpus=5:mem=15gb:scratch_local=100gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#copy files to scratch
cd /auto/brno3-cerit/nfs4/home/kika/pelomyxa/genome_assembly/
cp pelomyxa_clean.fa $SCRATCHDIR

cd /auto/brno3-cerit/nfs4/home/kika/pelomyxa/mapping/
cp pelo_clean_bw2_sorted.bam $SCRATCHDIR

cd /auto/brno2/home/kika/tools/rascaf/
cp rascaf $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

rascaf='rascaf'
assembly='pelomyxa_clean.fa'
bam_file='pelo_clean_bw2_sorted.bam'
base_name='pelo_clean_rascaf'

$rascaf -b $bam -f $assembly -o $base_name

#copy files back
cp *pelo_clean_rascaf* /auto/brno3-cerit/nfs4/home/kika/pelomyxa/mapping/.
