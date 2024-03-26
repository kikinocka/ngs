#!/bin/bash
#PBS -N Trinity
#PBS -l select=1:ncpus=30:mem=100gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
# module add trinity-2.11.0
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load trinity


workdir='/storage/brno12-cerit/home/kika/schizosaccharomyces_japonicus/'

#copy files to scratch
cp $workdir'reads/NG-A0875_Donna_1_trimmed_'*.fq.gz $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

fw='NG-A0875_Donna_1_trimmed_1.fq.gz'
rv='NG-A0875_Donna_1_trimmed_2.fq.gz'
out='donna1_trinity'

Trinity --seqType fq --left $fw --right $rv --output $out --max_memory 100G --CPU $PBS_NUM_PPN


#copy files back
rm *trimmed_*fq.gz
cp -r * $workdir
