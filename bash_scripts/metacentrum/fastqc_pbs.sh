#!/bin/sh
#PBS -N FastQC
#PBS -l select=1:ncpus=1:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe
#hashes explained: 
#-N job name, -q queue, -l select resources, -l walltime, -m ae, -j oe mail will be send at the end of the job

cat $PBS_NODEFILE

#add modules
module add fastQC-0.11.5

read_dir='/storage/brno3-cerit/home/kika/egracilis/'
out_dir='/storage/brno3-cerit/home/kika/egracilis/fastqc/'


#copy data to scratch
cp $read_dir'Dark_L004_R1.fastq.gz' $read_dir'Dark_L004_R2.fastq.gz' $read_dir'dark_trimmed_1.fq.gz' $read_dir'dark_trimmed_2.fq.gz' $SCRATCHDIR


#chdir to scratch and perform operations
cd $SCRATCHDIR
# fastqc -o $out_dir 'Light_L004_R1.fastq.gz'
# fastqc -o $out_dir 'Light_L004_R2.fastq.gz'
# fastqc -o $out_dir 'light_trimmed_1.fq.gz'
# fastqc -o $out_dir 'light_trimmed_2.fq.gz'

fastqc -o $out_dir 'Dark_L004_R1.fastq.gz'
fastqc -o $out_dir 'Dark_L004_R2.fastq.gz'
fastqc -o $out_dir 'dark_trimmed_1.fq.gz'
fastqc -o $out_dir 'dark_trimmed_2.fq.gz'
