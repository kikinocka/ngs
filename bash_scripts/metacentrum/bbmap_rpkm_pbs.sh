#!/bin/sh
#PBS -N bbmap_rpkm
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bbmap-36.92

data='/storage/brno3-cerit/home/kika/egracilis/'

#copy files to scratch
cp $data'GEFR01.1.fsa_nt' $SCRATCHDIR
cp $data'dark_trimmed_1.fq.gz' $SCRATCHDIR
cp $data'dark_trimmed_2.fq.gz' $SCRATCHDIR

assembly='GEFR01.1.fsa_nt'
fw='dark_trimmed_1.fq.gz'
rv='dark_trimmed_2.fq.gz'
# all='el_reads_new.fa'

sam='eg_dark_bbmap_rna.sam'
rpkm='eg_dark_bbmap.rpkm'
report='eg_dark_bbmap.report'


#compute on scratch
cd $SCRATCHDIR
#separate read files
bbmap.sh in=$fw in2=$rv out=$sam ref=$assembly rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report

#one read file
# bbmap.sh in=$all out=$sam ref=$assembly rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report


#copy files back
rm $assembly $fw $rv
# rm $assembly $all
cp -r * $data
