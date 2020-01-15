#!/bin/sh
#PBS -N bbmap_rpkm
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bbmap-36.92

data='/storage/brno3-cerit/home/kika/elonga/'

#copy files to scratch
cp $data'el_merged.fasta' $SCRATCHDIR
cp $data'el_reads_new.fa' $SCRATCHDIR

assembly='el_merged.fasta'
# fw='35all_1.fq.gz'
# rv='35all_2.fq.gz'
all='el_reads_new.fa'

sam='elonga_bbmap_rna.sam'
rpkm='elonga_bbmap.rpkm'
report='elonga_bbmap.report'


#compute on scratch
cd $SCRATCHDIR
#separate read files
# bbmap.sh in=$fw in2=$rv out=$sam ref=$assembly rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report

#one read file
bbmap.sh in=$all out=$sam ref=$assembly rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report


#copy files back
rm $assembly $fw $rv
cp -r * $data
