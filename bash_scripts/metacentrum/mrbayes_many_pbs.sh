#!/bin/sh
#PBS -N mrbayes-many
#PBS -l select=1:ncpus=4:mem=100gb:scratch_local=1gb:os=debian11
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add mrbayes-3.2.7a

data='/storage/brno3-cerit/home/kika/trafficking/TBCs/ver6/MrBayes2'

#copy files to scratch
cp $data'/'*.nex $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for aln in *.nex; do
	echo $aln
	mpirun -np 4 mb -i $aln
done


#copy files back
rm *.nex
cp -R * $data
