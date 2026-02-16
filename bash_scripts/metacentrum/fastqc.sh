#!/bin/sh
#PBS -N FastQC
#PBS -l select=1:ncpus=10:mem=10gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module load fastqc

read_dir='/storage/brno12-cerit/home/kika/pkld/second'


#copy data to scratch
cp $read_dir'/'*fastq.gz $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for file in *.gz; do
	echo $file
	fastqc -t $PBS_NUM_PPN -o $SCRATCHDIR $file
done

#copy files back
rm *gz
cp -r * $read_dir'/fastqc/'
