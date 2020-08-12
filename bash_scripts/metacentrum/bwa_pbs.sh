#!/bin/bash
#PBS -N bwa
#PBS -l select=1:ncpus=25:mem=50gb:scratch_local=100gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bwa-0.7.17
module add samtools-1.3.1

sags='/storage/brno3-cerit/home/kika/sags/mapping/EU2/'
outdir=$sags'bwa/'

#copy files to scratch
cp $spades'EU2_contigs.fasta' $SCRATCHDIR
cp $sags'EU2_r1_val_1.fq.gz' $sags'EU2_r2_val_2.fq.gz' $sags'unpaired_all.fq.gz' $SCRATCHDIR

assembly='EU2_contigs.fasta'
fw='EU2_r1_val_1.fq.gz'
rv='EU2_r2_val_2.fq.gz'
unpaired='unpaired_all.fq.gz'

base_name='EU2_bwa_'
index_report=$base_name'index_genome.report'

stat_mapped_paired=$base_name'mapped_paired.flagstat'
sorted_mapped_paired=$base_name'mapped_paired.sorted.bam'
bai_mapped_paired=$base_name'mapped_paired.sorted.bam.bai'

stat_mapped_unpaired=$base_name'mapped_unpaired.flagstat'
sorted_mapped_unpaired=$base_name'mapped_unpaired.sorted.bam'
bai_mapped_unpaired=$base_name'mapped_unpaired.bam.bai'

bam=$base_name'mapped_all.bam'
sorted=$base_name'mapped_all.sorted.bam'


#compute on scratch
cd $SCRATCHDIR
bwa index -a bwtsw $assembly 2>$index_report

bwa mem -t $PBS_NUM_PPN $assembly $fw $rw \
	| tee >(samtools flagstat - > $stat_mapped_paired) \
	| samtools sort -O BAM \
	| tee $sorted_mapped_paired \
	| samtools index - $bai_mapped_paired

bwa mem -t $PBS_NUM_PPN $assembly $fw $rw \
	| tee >(samtools flagstat - > $stat_mapped_unpaired) \
	| samtools sort -O BAM \
	| tee $sorted_mapped_unpaired \
	| samtools index - $bai_mapped_unpaired

samtools merge -@ $PBS_NUM_PPN -f $bam $sorted_mapped_paired $sorted_mapped_unpaired
samtools sort -@ $PBS_NUM_PPN -o $sorted $bam
samtools index $sorted

#copy files back
rm $assembly $fw $rv $unpaired
cp * $outdir
