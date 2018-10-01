#!/bin/bash
#PBS -N SPAdes
#PBS -l select=1:ncpus=16:ompthreads=16:mem=250gb:scratch_local=50gb:os=debian8 
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe
cat $PBS_NODEFILE

#add modules
module add spades-3.11.1

read_dir='/storage/brno3-cerit/home/kika/pelomyxa/reads/genome/deep_hiseq/'
outdir='/storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/deep_hiseq/p1/'

#copy reads to scratch
cd $read_dir
cp p1_trimmed_1.fq.gz p1_trimmed_2.fq.gz $SCRATCHDIR

fw='p1_trimmed_1.fq.gz'
rv='p1_trimmed_2.fq.gz'
report='p1_spades_report.txt'

#compute on scratch
cd $SCRATCHDIR
spades.py --pe1-1 $fw --pe1-2 $rv --careful -t 16 -m 250 -o out 2> $report

#copy results to your folder
cd out
cp -R * $outdir
cp ../$report $outdir
