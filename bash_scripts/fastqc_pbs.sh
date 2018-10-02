#!/bin/sh
#PBS -N FastQC
#PBS -l select=1:ncpus=1:mem=50gb:scratch_local=100gb
#PBS -l walltime=1:00:00
#PBS -m ae
#PBS -j oe
#hashes explained: 
#-N job name, -q queue, -l select resources, -l walltime, -m ae, -j oe mail will be send at the end of the job

#get name of the machine where the job is run
cat $PBS_NODEFILE

read_dir='/storage/brno3-cerit/home/kika/pelomyxa/reads/genome/preliminary_seq/'
out_dir='/storage/brno3-cerit/home/kika/pelomyxa/reads/genome/preliminary_seq/fastqc/'

# #just in case scratch is not created, but never happened to me:
# if [ ! -d "$SCRATCHDIR" ] ; then echo "Scratch directory is not created!" 1>&2; exit 1; fi
# echo $SCRATCHDIR
# trap 'clean_scratch' TERM EXIT

#load modules, may not be necessary
#https://wiki.metacentrum.cz/wiki/FastQC
module add fastQC-0.11.5

#copy data to scratch
cd $read_dir
cp pelo2_001_trimmed_1.fq.gz pelo2_001_trimmed_2.fq.gz pelo5_001_trimmed_1.fq.gz pelo5_001_trimmed_2.fq.gz $SCRATCHDIR


#chdir to scratch and perform operations
cd $SCRATCHDIR
fastqc -o $out_dir 'pelo2_001_trimmed_1.fq.gz'
fastqc -o $out_dir 'pelo2_001_trimmed_2.fq.gz'
fastqc -o $out_dir 'pelo5_001_trimmed_1.fq.gz'
fastqc -o $out_dir 'pelo5_001_trimmed_2.fq.gz'
