#!/bin/sh
#PBS -N bbmap_rpkm
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bbmap-36.92

assembly_dir='/storage/brno12-cerit/home/kika/p57/transcriptome/'
read_dir='/storage/brno12-cerit/home/kika/p57/hisat2/'

#copy files to scratch
cp $assembly_dir'p57_GG_trinity.fasta' $SCRATCHDIR
cp $read_dir'p57_trimmed_1.fq.gz' $SCRATCHDIR
cp $read_dir'p57_trimmed_2.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
assembly='p57_GG_trinity.fasta'
fw='p57_trimmed_1.fq.gz'
rv='p57_trimmed_2.fq.gz'
# all='el_reads_new.fa'

base=${assembly%fasta}ht2.
sam=$base'sam'
rpkm=$base'rpkm_bbmap.txt'
report=$base'report_bbmap.txt'

#separate read files
bbmap.sh in=$fw in2=$rv out=$sam ref=$assembly rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report

#one read file
# bbmap.sh in=$all out=$sam ref=$assembly rpkm=$rpkm threads=$PBS_NUM_PPN 2> $report


#copy files back
rm $assembly $fw $rv
# rm $assembly $all
cp -r * $read_dir
