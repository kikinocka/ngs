#!/bin/bash
#PBS -N Trinity
#PBS -l select=1:ncpus=30:mem=100gb:scratch_local=50gb
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add trinity-2.6.5

read_dir='/storage/brno3-cerit/home/kika/archamoebae/rhizomastix_libera/trimmed_reads'
out_dir='/storage/brno3-cerit/home/kika/archamoebae/rhizomastix_libera/'

#copy files to scratch
cp $read_dir'/'*trimmed_*.fq.gz $SCRATCHDIR

fw=SRR5396411_trimmed_1.fq.gz,SRR5396412_trimmed_1.fq.gz
rv=SRR5396411_trimmed_2.fq.gz,SRR5396412_trimmed_2.fq.gz


#compute on scratch
cd $SCRATCHDIR
Trinity --seqType fq --left $fw --right $rv --max_memory 100G --CPU $PBS_NUM_PPN

#copy files back
rm *trimmed_*fq.gz
cp -r * $out_dir
