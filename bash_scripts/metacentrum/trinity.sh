#!/bin/bash
#PBS -N Trinity
#PBS -l select=1:ncpus=30:mem=100gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load trinity


workdir='/storage/brno12-cerit/home/kika/trimastix/'

#copy files to scratch
cp $workdir'reads/SRR4017103_trimmed50_'*.fq.gz $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

fw='SRR4017103_trimmed50_1.fq.gz'
rv='SRR4017103_trimmed50_2.fq.gz'
out='Tmar_trinity'

Trinity --seqType fq --left $fw --right $rv --output $out --max_memory 100G --CPU $PBS_NUM_PPN


#copy files back
rm *trimmed_*fq.gz
cp -r * $workdir
