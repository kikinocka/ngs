#!/bin/bash
#PBS -N Bowtie2
#PBS -l select=1:ncpus=8:mem=15gb:scratch_local=100gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe


cat $PBS_NODEFILE

#add module
module add bowtie2-2.3.0
module add samtools-1.3.1

#copy files to scratch
cd /auto/brno3-cerit/nfs4/home/kika/pelomyxa/genome_assembly/all_reads/
cp contigs.fasta $SCRATCHDIR

cd /auto/brno3-cerit/nfs4/home/kika/pelomyxa/reads/transcriptome/
cp *.fq.gz $SCRATCHDIR

base_name='pelo_unclean_bw2'
ref='contigs.fasta'
bowtie2-build --threads $PBS_NUM_PPN $ref $base_name

p1_1='pelo1_trimmed_1.fq.gz','pelo2_trimmed_1.fq.gz','pelo3_trimmed_1.fq.gz','pelo5_trimmed_1.fq.gz','pelo6_trimmed_1.fq.gz'
p1_2='pelo1_trimmed_2.fq.gz','pelo2_trimmed_2.fq.gz','pelo3_trimmed_2.fq.gz','pelo5_trimmed_2.fq.gz','pelo6_trimmed_2.fq.gz'

samfile=$base_name'.sam'
report=$base_name'.txt'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq'
unmapped_paired=$base_name'_unmapped_paired.fq'

bowtie2 --very-sensitive -p $PBS_NUM_PPN -x $base_name -1 $p1_1 -2 $p1_2 --un-gz $unmapped_unpaired --un-conc-gz $unmapped_paired -S $samfile 2> $report

bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted'
sorted_file=$sorted'.bam'

samtools view -bS $samfile > $bamfile -@ $PBS_NUM_PPN
samtools sort $bamfile $sorted -@ $PBS_NUM_PPN
samtools index $sorted_file

#copy files back
cp $samfile /auto/brno3-cerit/nfs4/home/kika/pelomyxa/mapping/.
cp $sorted_file /auto/brno3-cerit/nfs4/home/kika/pelomyxa/mapping/.
cp $report /auto/brno3-cerit/nfs4/home/kika/pelomyxa/mapping/.
