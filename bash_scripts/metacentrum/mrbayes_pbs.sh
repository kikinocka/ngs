#!/bin/sh
#PBS -N mrbayes
#PBS -l select=1:ncpus=4:mem=100gb:scratch_local=1gb:os=debian11
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add mrbayes-3.2.7a

data='/storage/brno3-cerit/home/kika/trafficking/COPII/ver7/MrBayes/'

#copy files to scratch
cp $data'sec24.coded.trimal_gt-0.8.nex' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

#proteins
aln='sec24.coded.trimal_gt-0.8.nex'

mpirun -n $PBS_NUM_PPN mb-mpi $aln


#copy files back
rm $aln
cp -R * $data
