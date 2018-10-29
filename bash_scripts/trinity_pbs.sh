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
cp pelo6_trimmed_1.fq.gz pelo6_trimmed_2.fq.gz $SCRATCHDIR

fw='pelo6_trimmed_1.fq.gz'
rv='pelo6_trimmed_2.fq.gz'
report='pelo6_report.txt'

#compute on scratch
cd $SCRATCHDIR
Trinity --seqType fq --left $fw --right $rv --output pelo6_trinity --max_memory 50G --CPU 15 2> $report

cp $report pelo6_trinity/
cp -r pelo6_trinity/ $outdir
