#!/bin/sh
#PBS -N qualimap
#PBS -q default
#PBS -l select=1:ncpus=30:mem=50gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module ad qualiMap-11_12-16

mapping='/storage/brno3-cerit/home/kika/p57/jaculum/bw2/'
outdir='/storage/brno3-cerit/home/kika/p57/jaculum/'

#copy files to scratch
cp $mapping'jac.bw2_sorted.bam' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

bam='jac.bw2_sorted.bam'
qualimap bamqc -nt $PBS_NUM_PPN -bam $bam -outdir $SCRATCHDIR -outformat pdf

#copy files back
rm $bam
cp -r * $outdir
