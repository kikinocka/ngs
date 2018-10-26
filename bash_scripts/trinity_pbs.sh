#!/bin/bash
#PBS -N Trinity
#PBS -l select=1:ncpus=15:mem=50gb:scratch_local=100gb
#PBS -l walltime=30:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add trinity-2.6.5

read_dir='/storage/brno3-cerit/home/kika/pelomyxa/reads/transcriptome/'
out_dir='/storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/'

#copy reads to scratch
cd $read_dir
cp pelo5_trimmed_1.fq.gz pelo5_trimmed_2.fq.gz $SCRATCHDIR

fw='pelo5_trimmed_1.fq.gz'
rv='pelo5_trimmed_2.fq.gz'
report='pelo5_report.txt'

#compute on scratch
cd $SCRATCHDIR
Trinity --seqType fq --left $fw --right $rv --output pelo5_trinity --max_memory 50G --CPU 15 2> $report

cp $report pelo5_trinity/
cp -r pelo5_trinity/ $outdir
