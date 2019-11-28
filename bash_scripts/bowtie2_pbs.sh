#!/bin/bash
#PBS -N Bowtie2
#PBS -l select=1:ncpus=25:mem=100gb:scratch_local=120gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bowtie2-2.3.0
module add samtools-1.3.1

data='/storage/brno3-cerit/home/kika/pelomyxa/'
reads=$data'reads/genome/'
spades=$data'genome_assembly/'
outdir=$data'mapping/bowtie2/DNA_to_genome/'

#copy files to scratch
cp $spades'pelomyxa_final_genome.fa' $SCRATCHDIR
cp $reads'all_trimmed_1.fq.gz' $reads'all_trimmed_2.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

base_name='pelo_DNA_bw2'
ref='pelomyxa_final_genome.fa'
p1_1='all_trimmed_1.fq.gz'
p1_2='all_trimmed_2.fq.gz'
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
