#!/bin/sh
#PBS -N ra
#PBS -q default
#PBS -l select=1:ncpus=20:mem=70gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add ra-032020

data='/storage/brno3-cerit/home/kika/kinetoplastids/lmex_genome/ku70/'

#copy files to scratch
cp $data'reads/ku70_pacbio_all.fq.gz' $SCRATCHDIR
cp $data'reads/ku70_illumina_all.fq.gz' $SCRATCHDIR

tgs='ku70_pacbio_all.fq.gz'
hiseq='ku70_illumina_all.fq.gz'
report='ku70_ra_report.txt'
assembly='ku70_ra.fa'

#run on scratch
cd $SCRATCHDIR
ra -t $PBS_NUM_PPN -x pb $tgs $hiseq > $assembly 2> $report

#copy files back
rm $tgs $hiseq
cp -r * $data
