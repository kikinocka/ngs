#!/bin/sh
#PBS -N bbmap_rpkm
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bbmap-36.92

data='/storage/brno3-cerit/home/kika/kinetoplastids/lpyr_genome/bw2_mapping/'

#copy files to scratch
cp $data'lpyr_bw2.sam' $SCRATCHDIR

sam='lpyr_bw2.sam'
stat='lpyr_bw2.stat.txt'
hist='lpyr_bw2.hist.txt'
report='lpyr_bw2.pileup.report'


#compute on scratch
cd $SCRATCHDIR
pileup.sh in=$sam out=$stat hist=$hist 2> $report


#copy files back
rm $sam
cp -r * $data
