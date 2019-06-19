#!/bin/bash
#PBS -N create_hints
#PBS -l select=1:ncpus=5:mem=25gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add samtools-1.3.1

#copy files to scratch
datadir='/storage/brno3-cerit/home/kika/pelomyxa/mapping/tophat2/for_augustus/'
cp $datadir'accepted_hits.s.bam' $SCRATCHDIR
cp $datadir'accepted_hits.sf.bam' $SCRATCHDIR
cp $datadir'accepted_hits.both.ssf.bam' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
sorted='accepted_hits.s.bam'
filtered='accepted_hits.sf.bam'
both='accepted_hits.both.ssf.bam'

samtools index $sorted
samtools index $filtered
samtools index $both

#copy files back
rm *.bam
cp *.bam.bai $datadir
