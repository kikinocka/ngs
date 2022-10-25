#!/bin/bash
#PBS -N mfannot
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE


datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/mito'

#copy files to scratch
cp $datadir'/'*.fasta $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

export SINGULARITY_TMPDIR=$SCRATCHDIR
singularity build mfannot.sif docker://nbeck/mfannot

for file in *.fasta ; do
	echo $file
	base=${file%_scaffolds.fasta}

	singularity exec mfannot.sif mfannot --sqn --tbl --partial -o $base.out -l $base.log $file
done

#copy files back
rm *.fasta
cp * $datadir
