#!/bin/bash
#PBS -N Bowtie2
#PBS -l select=1:ncpus=50:mem=50gb:scratch_local=15gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bowtie2-2.4.2
module add samtools-1.11

assembly_dir='/storage/brno3-cerit/home/kika/ciliates/condylostoma/'
read_dir=$assembly_dir'reads/'
mapping_dir=$assembly_dir'mapping/'

#copy files to scratch
cp $assembly_dir'GCA_001499635.1_Condy_MAC_genomic.fna' $SCRATCHDIR
cp $read_dir'all_reads_trimmed.fq.gz' $SCRATCHDIR
# cp $read_dir'BML_October2016_trimmed_R.fastq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

base_name='condy'
ref='GCA_001499635.1_Condy_MAC_genomic.fna'
p1_1='all_reads_trimmed.fq.gz'
# p1_2='BML_October2016_trimmed_R.fastq.gz'
# r1='EU2_r1_unpaired_1.fq.gz'
# r2='EU2_r2_unpaired_2.fq.gz'

samfile=$base_name'.sam'
mapped=$base_name'_mapped.fq.gz'
# unmapped_unpaired=$base_name'_unmapped_unpaired.fq.gz'
# unmapped_paired=$base_name'_unmapped_paired.fq.gz'
unaligned=$base_name'_unaligned.fq.gz'
report=$base_name'.report.txt'
bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

bowtie2-build --threads $PBS_NUM_PPN $ref $base_name

# #paired-end reads
# bowtie2 --very-sensitive -p $PBS_NUM_PPN \
# 	-x $base_name \
# 	-1 $p1_1 \
# 	-2 $p1_2 \
# 	--un-gz $unmapped_unpaired \
# 	--un-conc-gz $unmapped_paired \
# 	--al-conc-gz $mapped \
# 	-S $samfile 2> $report
# 	# -U $r1,$r2 \
# 	#--no-unal \ #writes only mapped reads to sam file

#single reads
bowtie2 --very-sensitive -p $PBS_NUM_PPN \
	-x $base_name \
	-U $p1_1 \
	--al-gz $mapped \
	--un-gz $unaligned \
	-S $samfile 2> $report

# samtools view -bS -F 4 $samfile > $bamfile -@ $PBS_NUM_PPN #writes only mapped reads to bamfile
samtools view -bS -@ $PBS_NUM_PPN $samfile > $bamfile
samtools sort -o $sorted -@ $PBS_NUM_PPN $bamfile 
samtools index -b $sorted

#copy files back
cp *bw2* $mapping_dir
