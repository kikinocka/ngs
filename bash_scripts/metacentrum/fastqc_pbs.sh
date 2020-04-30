#!/bin/sh
#PBS -N FastQC
#PBS -l select=1:ncpus=1:mem=10gb:scratch_local=30gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add fastQC-0.11.5

read_dir='/storage/brno3-cerit/home/kika/prototheca/wickerhamii'
out_dir='/storage/brno3-cerit/home/kika/prototheca/wickerhamii/fastqc/'


#copy data to scratch
cp $read_dir'/'*trimmed*.gz $SCRATCHDIR


#chdir to scratch and perform operations
cd $SCRATCHDIR

files='*.gz'

for file in $files; do
	echo $file
	fastqc -o $SCRATCHDIR $file
done

#copy files back
rm $files
cp -r * $out_dir
