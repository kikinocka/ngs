#!/bin/bash
#PBS -N CCMetagen
#PBS -l select=1:ncpus=20:mem=10gb:scratch_local=1gb
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

echo 'from ete3 import NCBITaxa; ncbi = NCBITaxa(); ncbi.update_taxonomy_database(); quit()' > run.py
python run.py

CCMetagen.py -i $kma -o $out

#copy files back
rm $kma
cp -R * $datadir
