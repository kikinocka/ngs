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

sags='/storage/brno3-cerit/home/kika/sags/reassembly/'
reads=$sags'trimmed_reads/'
spades=$sags'spades/'
outdir=$sags'mapping_bowtie2/'

#copy files to scratch
cp $spades'contigs.fasta' $SCRATCHDIR
cp $reads'all_r1_trimmed.fq.gz' $reads'all_r2_trimmed.fq.gz' $reads'all_unpaired.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

base_name='EU1718_bw2_'
ref='contigs.fasta'
p1_1='all_r1_trimmed.fq.gz'
p1_2='all_r2_trimmed.fq.gz'
unpaired='all_unpaired.fq.gz'
samfile=$base_name'.sam'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq'
unmapped_paired=$base_name'_unmapped_paired.fq'
report=$base_name'_report.txt'

bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

bowtie2-build --threads $PBS_NUM_PPN $ref $base_name
bowtie2 --very-sensitive -p $PBS_NUM_PPN -x $base_name -1 $p1_1 -2 $p1_2 -r $unpaired \
--un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $samfile 2> $report

samtools view -bS $samfile > $bamfile -@ $PBS_NUM_PPN
samtools sort -o $sorted -@ PBS_NUM_PPN $bamfile 
samtools index $sorted

#copy files back
cp *bw2* $data_dir'pilon5/'
