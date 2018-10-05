#!/bin/bash
#PBS -N SPAdes
#PBS -l select=1:ncpus=20:ompthreads=20:mem=250gb:scratch_local=50gb
#PBS -l walltime=15:00:00
#PBS -m ae
#PBS -j oe
cat $PBS_NODEFILE

#add modules
module add spades-3.11.1

read_dir='/storage/brno3-cerit/home/kika/pelomyxa/reads/genome/deep_hiseq/'
outdir='/storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/deep_hiseq/p2/k127/'

#copy reads to scratch
cd $read_dir
cp p2_trimmed_1.fq.gz p2_trimmed_2.fq.gz $SCRATCHDIR

fw='p2_trimmed_1.fq.gz'
rv='p2_trimmed_2.fq.gz'
report='p2_spades_report.txt'

#compute on scratch
cd $SCRATCHDIR
spades.py --pe1-1 $fw --pe1-2 $rv --careful -k 127 -t 20 -m 250 -o out 2> $report

#copy results to your folder
cd out
cp -R * $outdir
cp ../$report $outdir
