#!/bin/bash
#PBS -N SPAdes
#PBS -l select=1:ncpus=20:ompthreads=20:mem=250gb:scratch_local=50gb
#PBS -l walltime=8:00:00
#PBS -m ae
#PBS -j oe
cat $PBS_NODEFILE

#add modules
module add spades-3.11.1

read_dir='/auto/brno3-cerit/nfs4/home/kika/pelomyxa/reads/genome/deep_hiseq/'
outdir='/storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/deep_hiseq/p5/'

#copy reads to scratch
cd $read_dir
cp p5_trimmed_1.fq.gz p5_trimmed_2.fq.gz $SCRATCHDIR

fw='p5_trimmed_1.fq.gz'
rv='p5_trimmed_2.fq.gz'
report='p5_spades_report.txt'

#compute on scratch
cd $SCRATCHDIR
spades.py --pe1-1 $fw --pe1-2 $rv --careful -k 127 -t 20 -m 250 -o out 2> $report

#copy results to your folder
cd out
cp -R * $outdir
cp ../$report $outdir
