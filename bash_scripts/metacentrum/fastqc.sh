#!/bin/sh
#PBS -N FastQC
#PBS -l select=1:ncpus=1:mem=10gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load fastQC

read_dir='/storage/brno3-cerit/home/kika/amoebophrya/reads'


#copy data to scratch
cp $read_dir'/'*trimmed* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for file in *.gz; do
	echo $file
	fastqc -o $SCRATCHDIR $file
done

#copy files back
rm *gz
cp -r * $read_dir'/fastqc/'
