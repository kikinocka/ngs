#!/bin/bash
#PBS -N Trinity
#PBS -l select=1:ncpus=30:mem=100gb:scratch_local=50gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add trinity-2.11.0

read_dir='/storage/brno3-cerit/home/kika/blasto_comparative/sp_HR-05/transcriptome_reads/'
out_dir='/storage/brno3-cerit/home/kika/blasto_comparative/trinity/'

#copy files to scratch
cp $read_dir'/'*trimmed_*.fq.gz $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

fw='braa_trimmed_1.fq.gz'
rv='braa_trimmed_2.fq.gz'

Trinity --seqType fq --left $fw --right $rv --max_memory 100G --CPU $PBS_NUM_PPN


#copy files back
rm *trimmed_*fq.gz
cp -r * $out_dir
