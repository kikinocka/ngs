#!/bin/sh
#PBS -N FastQC
#PBS -l select=1:ncpus=1:mem=50gb:scratch_local=20gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add fastQC-0.11.5

read_dir='/storage/brno3-cerit/home/kika/prototheca/wickerhamii'
out_dir='/storage/brno3-cerit/home/kika/prototheca/wickerhamii/fastqc/'


#copy data to scratch
cp $read_dir'/'*.gz $SCRATCHDIR


#chdir to scratch and perform operations
cd $SCRATCHDIR

files='*.gz'

for file in $files; do
	echo $file
	fastqc -o $out_dir $file
done


# fastqc -o $out_dir 'Light_L004_R1.fastq.gz'
# fastqc -o $out_dir 'Light_L004_R2.fastq.gz'
# fastqc -o $out_dir 'light_trimmed_1.fq.gz'
# fastqc -o $out_dir 'light_trimmed_2.fq.gz'
