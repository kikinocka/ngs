#!/bin/bash
#PBS -N Bowtie2
#PBS -l select=1:ncpus=25:mem=50gb:scratch_local=100gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bowtie2-2.3.0
module add samtools-1.3.1

#copy files to scratch
data_dir='/storage/brno3-cerit/home/kika/p57/'

cp $data_dir'pilon4/p57_pilon4.fa' $SCRATCHDIR
cp $data_dir'p57_trimmed_1.fq' $SCRATCHDIR
cp $data_dir'p57_trimmed_2.fq' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

base_name='p57_pilon4_bw2'
ref='p57_pilon4.fa'
p1_1='p57_trimmed_1.fq'
p1_2='p57_trimmed_2.fq'

samfile=$base_name'.sam'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq'
unmapped_paired=$base_name'_unmapped_paired.fq'
report=$base_name'_report.txt'

bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

bowtie2-build --threads $PBS_NUM_PPN $ref $base_name
bowtie2 --very-sensitive -p $PBS_NUM_PPN -x $base_name -1 $p1_1 -2 $p1_2 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $samfile 2> $report

samtools view -bS $samfile > $bamfile -@ $PBS_NUM_PPN
samtools sort -o $sorted -@ PBS_NUM_PPN $bamfile 
samtools index $sorted

#copy files back
cp *bw2* $data_dir'pilon4/'
