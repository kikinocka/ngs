#!/bin/sh
#PBS -N FastQC
#PBS -l select=1:ncpus=1:mem=10gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add fastQC-0.11.5

read_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenome'


#copy data to scratch
cp $read_dir'/'*.gz $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

files='*.gz'

for file in $files; do
	echo $file
	fastqc -o $SCRATCHDIR $file
done

#copy files back
rm $files
cp -r * $read_dir'/fastqc/'
