#!/bin/bash
#PBS -N Bowtie2
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bowtie2-2.3.0
module add samtools-1.3.1

data='/storage/brno3-cerit/home/kika/tbruc/'
outdir=$data'bw2_mapping/'

#copy files to scratch
cp $data'tbruc_genome.fa' $SCRATCHDIR
cp $data'tbruc_trimmed_1.fq.gz' $data'tbruc_trimmed_2.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

base_name='tbruc_bw2'
ref='tbruc_genome.fa'
p1_1=$reads'tbruc_trimmed_1.fq.gz'
p1_2=$reads'tbruc_trimmed_2.fq.gz'
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
cp *bw2* $outdir
