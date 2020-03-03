#!/bin/sh
#PBS -N ra
#PBS -q default
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add ra-032020

data='/storage/brno3-cerit/home/kika/kinetoplastids/lmex_genome/ku80/'

#copy files to scratch
cp $data'reads/ku80_pacbio_all.fq.gz' $SCRATCHDIR
cp $data'reads/ku80_illumina_all.fq.gz' $SCRATCHDIR

tgs='ku80_pacbio_all.fq.gz'
hiseq='ku80_illumina_all.fq.gz'
report='ku80_ra_report.txt'

#run on scratch
cd $SCRATCHDIR
ra -t $PBS_NUM_PPN -x pb $tgs $hiseq 2> $report

#copy files back
rm $tgs $hiseq
cp -r * $data
