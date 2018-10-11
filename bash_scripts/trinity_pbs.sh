#!/bin/bash
#PBS -N Trinity
#PBS -l select=1:ncpus=20:mem=100gb:scratch_local=100gb
#PBS -l walltime=20:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add trinity-2.6.5

read_dir='/storage/brno3-cerit/home/kika/pelomyxa/reads/transcriptome/'
out_dir='/storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/pelo1/'

#copy reads to scratch
cd $read_dir
cp pelo1_trimmed_1.fq.gz pelo1_trimmed_2.fq.gz $SCRATCHDIR

fw='pelo1_trimmed_1.fq.gz'
rv='pelo1_trimmed_2.fq.gz'
report='pelo1_report.txt'

#compute on scratch
Trinity --seqType fq --left $fw --right $rv --output trinity_out --max_memory 100G --CPU 20 2> $report

cd trinity_out
cp -R * $outdir
cp ../$report $outdir
