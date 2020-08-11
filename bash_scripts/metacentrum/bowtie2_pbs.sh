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

data='/storage/brno3-cerit/home/kika/sags/mapping/EU2/'

#copy files to scratch
cp $data'EU2_contigs.fasta' $SCRATCHDIR
cp $data'EU2_r1_val_1.fq.gz' $SCRATCHDIR
cp $data'EU2_r2_val_2.fq.gz' $SCRATCHDIR
cp $data'EU2_r1_unpaired_1.fq.gz' $SCRATCHDIR
cp $data'EU2_r2_unpaired_2.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

base_name='EU2_bw2'
ref='EU2_contigs.fasta'
p1_1='EU2_r1_val_1.fq.gz'
p1_2='EU2_r2_val_2.fq.gz'
r1='EU2_r1_unpaired_1.fq.gz'
r2='EU2_r2_unpaired_2.fq.gz'

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
cp *bw2* $data
