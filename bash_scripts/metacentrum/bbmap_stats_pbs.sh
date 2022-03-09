#!/bin/sh
#PBS -N bbmap_rpkm
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bbmap-36.92

data='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/20200821_BML-P3B/metabinner/bins'

#copy files to scratch
cp $data'/'*.fa $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

statswrapper.sh *.fa

#copy files back
rm *.fa
cp -r * $data
