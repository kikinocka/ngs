#/bin/bash
#PBS -N datasethandler
#PBS -l select=1:ncpus=10:mem=20gb:scratch_local=2gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

# get name of the machine where the job is run
cat $PBS_NODEFILE

# add modules
module add python36-modules-gcc
module add iqtree-1.6.8
module add mafft-7.313
module add trimal-1.4

#copy files to scratch
DATADIR='/storage/brno3-cerit/home/kika/proteromonas/SOD_tree/ver2'

cp '/storage/brno2/home/kika/scripts/kika/py_scripts/datasethandler-server.py' $SCRATCHDIR
cp $DATADIR'/'*.fa $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
./datasethandler-server.py -a mafft -t iqtree -i batch -b -s

#copy files back
cp -R RESULT $DATADIR
cp -R temp $DATADIR
cp error.log $DATADIR
