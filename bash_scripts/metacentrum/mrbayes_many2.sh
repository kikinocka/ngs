#!/bin/sh
#PBS -N mrbayes-many2
#PBS -l select=1:ncpus=4:mem=20gb:scratch_local=1gb
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add mrbayes-3.2.7a

data='/storage/brno12-cerit/home/kika/kinetoplastids/AOX/ver5/mrbayes'

#copy files to scratch
cp $data'/'* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for aln in *.nex; do
	echo $aln
	mpirun -np $PBS_NUM_PPN mb -i $aln
done


#copy files back
rm *.nex
cp -R * $data
