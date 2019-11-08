#!/bin/sh
#PBS -N trim_galore
#PBS -l select=1:ncpus=8:mem=10gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add trim_galore-0.6.2

raw='/storage/brno3-cerit/home/kika/sags/reassembly/raw_reads/'
trimmed='/storage/brno3-cerit/home/kika/sags/reassembly/trimmed_reads/'

#copy data to scratch
cp $raw'EU18_r1.fq.gz' $raw'EU18_r2.fq.gz' $SCRATCHDIR

fw='EU18_r1.fq.gz'
rv='EU18_r2.fq.gz'
report='trim_galore_report.txt'


#run on scratch
cd $SCRATCHDIR
trim_galore -q 20 --fastqc --gzip --length 50 --paired --retain_unpaired --cores $PBS_NUM_PPN $fw $rv 2> $report

#copy files back
rm $fw $rv
cp -r * $trimmed
