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

read_dir='/storage/brno3-cerit/home/kika/tbruc/'
out_dir='/storage/brno3-cerit/home/kika/tbruc/fastqc/'


#copy data to scratch
cp $read_dir'ID-003057-NS091_R1_input.fq.gz' $read_dir'ID-003057-NS091_R2_input.fq.gz' $read_dir'tbruc_trimmed_1.fq.gz' $read_dir'tbruc_trimmed_2.fq.gz' $SCRATCHDIR


#chdir to scratch and perform operations
cd $SCRATCHDIR
fastqc -o $out_dir 'ID-003057-NS091_R1_input.fq.gz'
fastqc -o $out_dir 'ID-003057-NS091_R2_input.fq.gz'
fastqc -o $out_dir 'tbruc_trimmed_1.fq.gz'
fastqc -o $out_dir 'tbruc_trimmed_2.fq.gz'
