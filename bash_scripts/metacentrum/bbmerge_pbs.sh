#!/bin/sh
#PBS -N bbmerge
#PBS -l select=1:ncpus=10:mem=5gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bbmap-36.92

raw='/storage/brno3-cerit/home/kika/sl_euglenozoa/raw_reads/'
res='/storage/brno3-cerit/home/kika/sl_euglenozoa/merged_reads/'

#copy data to scratch
cp $raw'14_TGGTCA_L001_R1_001.fastq.bz2' $raw'14_TGGTCA_L001_R2_001.fastq.bz2' $SCRATCHDIR

fw='14_TGGTCA_L001_R1_001.fastq.bz2'
rv='14_TGGTCA_L001_R2_001.fastq.bz2'
merged='14_TGGTCA_merged.fq.gz'
un1='14_TGGTCA_unmerged_R1.fq.gz'
un2='14_TGGTCA_unmerged_R2.fq.gz'
report='14_TGGTCA_bbmerge_report.txt'


#run on scratch
cd $SCRATCHDIR
bbmerge.sh in1=$fw in2=$rv out=$merged outu1=$un1 outu2=$un2 minoverlap=10 ziplevel=9 t=$PBS_NUM_PPN 2>$report


#copy files back
rm $fw $rv
cp -r * $res
