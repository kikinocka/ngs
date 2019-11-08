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
cp $reads'EU17_r1_trimmed.fq.gz' $reads'EU17_r2_trimmed.fq.gz' $SCRATCHDIR

fw='EU17_r1_trimmed.fq.gz'
rv='EU17_r2_trimmed.fq.gz'
merged='EU17_trimmed_merged.fq.gz'
un1='EU17_r1_trimmed_unmerged.fq.gz'
un2='EU17_r2_trimmed_unmerged.fq.gz'
report='bbmerge_report.txt'


#run on scratch
cd $SCRATCHDIR
bbmerge.sh in1=$fw in2=$rv out=$merged outu1=$un1 outu2=$un2 minoverlap=10 ziplevel=9 t=$PBS_NUM_PPN 2>$report


#copy files back
rm $fw $rv
cp -r * $reads
