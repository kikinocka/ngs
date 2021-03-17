#!/bin/bash
#PBS -N Bowtie2
#PBS -l select=1:ncpus=30:mem=80gb:scratch_local=150gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bowtie2-2.4.2
module add samtools-1.11

assembly_dir='/storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/'
read_dir='/storage/brno3-cerit/home/kika/pelomyxa/reads/genome/'
mapping_dir='/storage/brno3-cerit/home/kika/pelomyxa/mapping/bowtie2/DNA_to_genome/'

#copy files to scratch
cp $assembly_dir'pelomyxa_final_corr_genome.fa' $SCRATCHDIR
cp $read_dir'all_trimmed_1.fq.gz' $SCRATCHDIR
cp $read_dir'all_trimmed_2.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

base_name='pelo_genome_bw2'
ref='pelomyxa_final_corr_genome.fa'
p1_1='all_trimmed_1.fq.gz'
p1_2='all_trimmed_2.fq.gz'
# r1='EU2_r1_unpaired_1.fq.gz'
# r2='EU2_r2_unpaired_2.fq.gz'

samfile=$base_name'.sam'
mapped=$base_name'_mapped.fq.gz'
unmapped_unpaired=$base_name'_unmapped_unpaired.fq.gz'
unmapped_paired=$base_name'_unmapped_paired.fq.gz'
report=$base_name'.report.txt'
bamfile=$base_name'_unsorted.bam'
sorted=$base_name'_sorted.bam'

bowtie2-build --threads $PBS_NUM_PPN $ref $base_name
bowtie2 --very-sensitive -p $PBS_NUM_PPN \
	-x $base_name \
	-1 $p1_1,$p2_1 \
	-2 $p1_2,$p2_2 \
	--un-gz $unmapped_unpaired \
	--un-conc-gz $unmapped_paired \
	--al-conc-gz $mapped \
	-S $samfile 2> $report
	# -U $r1,$r2 \
	#--no-unal \ #writes only mapped reads to sam file

# samtools view -bS -F 4 $samfile > $bamfile -@ PBS_NUM_PPN #writes only mapped reads to bamfile
samtools view -bS $samfile > $bamfile -@ $PBS_NUM_PPN
samtools sort -o $sorted -@ PBS_NUM_PPN $bamfile 
samtools index $sorted

#copy files back
cp *bw2* $mapping_dir
