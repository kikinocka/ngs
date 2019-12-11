#!/bin/sh
#PBS -N bbmerge
#PBS -l select=1:ncpus=10:mem=10gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bbmap-36.92

reads='/storage/brno3-cerit/home/kika/sags/reassembly/trimmed_reads/'

#copy data to scratch
cp $reads'EU18_r1_trimmed.fq.gz' $reads'EU18_r2_trimmed.fq.gz' $SCRATCHDIR

fw='EU18_r1_trimmed.fq.gz'
rv='EU18_r2_trimmed.fq.gz'
merged='EU18_trimmed_merged.fq.gz'
un1='EU18_r1_trimmed_unmerged.fq.gz'
un2='EU18_r2_trimmed_unmerged.fq.gz'
report='EU18_bbmerge_report.txt'


#run on scratch
cd $SCRATCHDIR
bbmerge.sh in1=$fw in2=$rv out=$merged outu1=$un1 outu2=$un2 minoverlap=10 ziplevel=9 t=$PBS_NUM_PPN 2>$report


#copy files back
rm $fw $rv
cp -r * $reads
