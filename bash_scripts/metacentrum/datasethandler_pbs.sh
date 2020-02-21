#/bin/bash
#PBS -N datasethandler
#PBS -l select=1:ncpus=10:mem=20gb:scratch_local=2gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe
# hashes explained: -N job name, -q queue, -l select resources, -l walltime, -m ae, -j oe mail will be send at the end of the job

# get name of the machine where the job is run
cat $PBS_NODEFILE

# #SCRATCH-related statements
# if [ ! -d '$SCRATCHDIR' ] ; then echo 'Scratch directory is not created!' 1>&2; exit 1; fi
# echo $SCRATCHDIR
# trap 'clean_scratch' TERM EXIT

# add modules
module add python36-modules-gcc
module add iqtree-1.6.8
module add mafft-7.313
module add trimal-1.4

#copy files to scratch
DATADIR='/storage/brno3-cerit/home/kika/proteromonas/PXMP2_tree/ver2'

cp '/storage/brno2/home/kika/scripts/kika/py_scripts/datasethandler-server.py' $SCRATCHDIR
cp $DATADIR'/'*.fa $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
./datasethandler-server.py -a mafft -t iqtree -i batch -b -s

#copy files back
cp -R RESULT $DATADIR
cp -R temp $DATADIR
cp error.log $DATADIR
