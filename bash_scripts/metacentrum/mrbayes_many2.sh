#!/bin/sh
#PBS -N mrbayes-many2
#PBS -l select=1:ncpus=4:mem=3gb:scratch_local=1gb:os=debian11
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module add mrbayes

data='/storage/brno3-cerit/home/kika/trafficking/diplonemids_all/Dsl1/mrbayes'

#copy files to scratch
cp $data'/rint1'* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for aln in *.nex; do
	echo $aln
	mpirun -np 4 mb -i $aln
done


#copy files back
rm *.nex
cp -R * $data
