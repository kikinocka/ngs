#!/bin/bash
#PBS -N CCMetagen
#PBS -l select=1:ncpus=20:mem=1gb:scratch_local=1gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add ccmetagen-1.2.5


datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/kma-ccmeta_assembly/'

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
