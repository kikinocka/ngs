#!/bin/bash
#PBS -N Bowtie2
#PBS -l select=1:ncpus=30:mem=50gb:scratch_local=20gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bowtie2-2.3.0
module add samtools-1.3.1

data='/storage/brno3-cerit/home/kika/sags/'
mapping=$data'mapping/EU18/'

#copy files to scratch
cp $mapping'EU18_contigs.fasta' $SCRATCHDIR
cp $data'reassembly/trimmed_reads/EU18_r1_trimmed.fq.gz' $SCRATCHDIR
cp $data'reassembly/trimmed_reads/EU18_r2_trimmed.fq.gz' $SCRATCHDIR
cp $data'reassembly/trimmed_reads/EU18_r1_unpaired_1.fq.gz' $SCRATCHDIR
cp $data'reassembly/trimmed_reads/EU18_r2_unpaired_2.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

base_name='EU18_bw2'
ref='EU18_contigs.fasta'
p1_1='EU18_r1_trimmed.fq.gz'
p1_2='EU18_r2_trimmed.fq.gz'
r1='EU18_r1_unpaired_1.fq.gz'
r2='EU18_r2_unpaired_2.fq.gz'

samfile=$base_name'.sam'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq'
unmapped_paired=$base_name'_unmapped_paired.fq'
report=$base_name'.report.txt'
bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

bowtie2-build --threads $PBS_NUM_PPN $ref $base_name
bowtie2 --very-sensitive -p $PBS_NUM_PPN \
	-x $base_name \
	-1 $p1_1 \
	-2 $p1_2 \
	-U $r1,$r2 \
	--un-gz $unmapped_unpaired \
	--un-conc-gz $unmapped_paired \
	-S $samfile 2> $report

samtools view -bS $samfile > $bamfile -@ $PBS_NUM_PPN
samtools sort -o $sorted -@ PBS_NUM_PPN $bamfile 
samtools index $sorted

#copy files back
cp *bw2* $mapping
