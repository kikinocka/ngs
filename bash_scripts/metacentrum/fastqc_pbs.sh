#!/bin/sh
#PBS -N FastQC
#PBS -l select=1:ncpus=1:mem=50gb:scratch_local=100gb
#PBS -l walltime=0:30:00
#PBS -m ae
#PBS -j oe
#hashes explained: 
#-N job name, -q queue, -l select resources, -l walltime, -m ae, -j oe mail will be send at the end of the job

cat $PBS_NODEFILE

#add modules
module add fastQC-0.11.5

read_dir='/storage/brno3-cerit/home/kika/sags/reassembly/trimmed_reads/'
out_dir='/storage/brno3-cerit/home/kika/sags/reassembly/trimmed_reads/fastqc/'

#copy data to scratch
cp $read_dir'EU17_r1_trimmed.fq.gz' $read_dir'EU17_r2_trimmed.fq.gz' $read_dir'EU18_r1_trimmed.fq.gz' $read_dir'EU18_r2_trimmed.fq.gz' $SCRATCHDIR


#chdir to scratch and perform operations
cd $SCRATCHDIR
fastqc -o $out_dir 'EU17_r1_trimmed.fq.gz'
fastqc -o $out_dir 'EU17_r2_trimmed.fq.gz'
fastqc -o $out_dir 'EU18_r1_trimmed.fq.gz'
fastqc -o $out_dir 'EU18_r2_trimmed.fq.gz'
