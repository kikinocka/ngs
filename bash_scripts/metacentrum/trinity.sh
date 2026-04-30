#!/bin/bash
#PBS -N Trinity
#PBS -l select=1:ncpus=30:mem=100gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE


workdir='/storage/brno12-cerit/home/kika/trimastix/'

#copy files to scratch
cp $workdir'reads/SRR4017103_trimmed_'*.fq.gz $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

fw='SRR4017103_trimmed_1.fq.gz'
rv='SRR4017103_trimmed_2.fq.gz'
out='Tmar_trinity'

singularity exec /cvmfs/singularity.metacentrum.cz/Trinity/trinityrnaseq.v2.15.2.simg Trinity \
	--seqType fq --left $fw --right $rv --output $out --max_memory 100G --CPU $PBS_NUM_PPN


#copy files back
rm *trimmed_*fq.gz
cp -r * $workdir
