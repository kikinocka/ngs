#!/bin/bash
#PBS -N CCMetagen
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add python36-modules-gcc


datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/kma-ccmeta/'

#copy files to scratch
cp $datadir'bml_kma.res' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

kma='bml_kma.res'
out='CCMetagen'

CCMetagen.py -i $kma -o $out

#copy files back
rm $kma
cp -R * $datadir
