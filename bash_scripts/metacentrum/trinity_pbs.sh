#!/bin/bash
#PBS -N Trinity
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=30gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add trinity-2.6.5

datadir='/storage/brno3-cerit/home/kika/prototheca/wickerhamii/'
outdir=$datadir'trinity/'
fw=$datadir'BILC_trimmed_1.fq.gz'
rv=$datadir'BILC_trimmed_2.fq.gz'

#copy reads to scratch
cp $fw $rv $SCRATCHDIR

report='pwic_trinity_report.txt'

#compute on scratch
cd $SCRATCHDIR
Trinity --seqType fq --left $fw --right $rv --max_memory 50G --CPU $PBS_NUM_PPN 2> $report

#copy files back
rm $fw $rv
cp -r * $outdir
