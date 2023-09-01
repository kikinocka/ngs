#!/bin/bash
#PBS -N Trinity
#PBS -l select=1:ncpus=30:mem=100gb:scratch_local=50gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
# module add trinity-2.11.0
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load trinity

read_dir='/storage/brno3-cerit/home/kika/UGA_decoding/nyctotherus/reads'
out_dir='/storage/brno3-cerit/home/kika/UGA_decoding/nyctotherus/trinity/'

#copy files to scratch
cp $read_dir'/'*trimmed_*.fq.gz $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

fw='all_trimmed_1.fq.gz'
rv='all_trimmed_2.fq.gz'

Trinity --seqType fq --left $fw --right $rv --max_memory 100G --CPU $PBS_NUM_PPN


#copy files back
rm *trimmed_*fq.gz
cp -r * $out_dir
