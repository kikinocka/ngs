#!/bin/bash
#PBS -N taxify_correction
#PBS -l select=1:ncpus=1:mem=80gb:scratch_local=50gb
#PBS -l walltime=2:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#copy files to scratch
cd /storage-brno2/home/kika/scripts/kika/py_scripts/
cp fucking_taxify_correction.py $SCRATCHDIR

cd /storage-brno3-cerit/home/kika/blobtools/
cp prot.accession2taxid $SCRATCHDIR

datadir='/storage-brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/blobtools/'
cd $datadir
cp pelo_trinity.not_taxified.out $SCRATCHDIR
cp pelo_trinity.taxified.out $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

python3 fucking_taxify_correction.py

#copy files back
cd pelo_trinity.taxified.out $datadir || export CLEAN_SCRATCH=false
