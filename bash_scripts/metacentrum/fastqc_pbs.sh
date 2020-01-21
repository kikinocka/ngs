#!/bin/sh
#PBS -N FastQC
#PBS -l select=1:ncpus=1:mem=50gb:scratch_local=100gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe
#hashes explained: 
#-N job name, -q queue, -l select resources, -l walltime, -m ae, -j oe mail will be send at the end of the job

cat $PBS_NODEFILE

#add modules
module add fastQC-0.11.5

read_dir='/storage/brno3-cerit/home/kika/lsey/'
out_dir='/storage/brno3-cerit/home/kika/lsey/fastqc/'


#copy data to scratch
cp $read_dir'14I_1.fastq.gz' $read_dir'14I_2.fastq.gz' $read_dir'14II_1.fastq.gz' $read_dir'14II_2.fastq.gz' $read_dir'14III_1.fastq.gz' $read_dir'14III_2.fastq.gz' $SCRATCHDIR
cp $read_dir'14I_trimmed_1.fq.gz' $read_dir'14I_trimmed_2.fq.gz' $read_dir'14II_trimmed_1.fq.gz' $read_dir'14II_trimmed_2.fq.gz' $read_dir'14III_trimmed_1.fq.gz' $read_dir'14III_trimmed_2.fq.gz' $SCRATCHDIR


#chdir to scratch and perform operations
cd $SCRATCHDIR
fastqc -o $out_dir '14I_1.fastq.gz'
fastqc -o $out_dir '14I_2.fastq.gz'
fastqc -o $out_dir '14II_1.fastq.gz'
fastqc -o $out_dir '14II_2.fastq.gz'
fastqc -o $out_dir '14III_1.fastq.gz'
fastqc -o $out_dir '14III_2.fastq.gz'

fastqc -o $out_dir '14I_trimmed_1.fq.gz'
fastqc -o $out_dir '14I_trimmed_2.fq.gz'
fastqc -o $out_dir '14II_trimmed_1.fq.gz'
fastqc -o $out_dir '14II_trimmed_2.fq.gz'
fastqc -o $out_dir '14III_trimmed_1.fq.gz'
fastqc -o $out_dir '14III_trimmed_2.fq.gz'
