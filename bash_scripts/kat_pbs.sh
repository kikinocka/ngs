#!/bin/bash
#PBS -N kat
#PBS -l select=1:ncpus=10:mem=5gb:scratch_local=100gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add kat-2.3.4

sags='/storage/brno3-cerit/home/kika/sags/reassembly/'
reads=$sags'trimmed_reads/'
outdir=$sags'reports/kat/'

#copy files to scratch
cp $reads'all_r1_trimmed.fq.gz' $reads'all_r2_trimmed.fq.gz' $reads'all_unpaired.fq.gz' $SCRATCHDIR

fw='all_r1_trimmed.fq.gz'
rv='all_r2_trimmed.fq.gz'
unpaired='all_unpaired.fq.gz'
report='kat.report'

#compute on scratch
cd $SCRATCHDIR
kat hist -o $SCRATCHDIR -d -t $PBS_NUM_PPN $fw $rv $unpaired 2> $report

#copy files back
rm $fw $rv $unpaired
cp * $outdir
