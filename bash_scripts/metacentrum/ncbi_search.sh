#!/bin/bash
#PBS -N ncbi_search
#PBS -l select=1:ncpus=1:mem=10gb:scratch_local=3gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load python

datadir='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/'
scriptdir='/storage/brno2/home/kika/scripts/py_scripts/databases/'


#copy files to scratch
cp $datadir'check_tax.acc' $SCRATCHDIR
cp $scriptdir'ncbi_search.py' $SCRATCHDIR

#run on scratch
cd $SCRATCHDIR

#Delete os.chdir in python script
script='ncbi_search.py'
python $script


#copy files back
rm *.acc
cp * $datadir
