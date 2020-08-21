#!/bin/bash
#PBS -N bwa
#PBS -l select=1:ncpus=25:mem=20gb:scratch_local=20gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add bwa-0.7.17
module add samtools-1.3.1

sags='/storage/brno3-cerit/home/kika/sags/reassembly/'
reads=$sags'trimmed_reads/'
outdir=$sags'mapping/bwa_joined_contigs2/'

#copy files to scratch
cp $sags'EU1718_contigs_joined_2.fa' $SCRATCHDIR
cp $reads'all_r1_trimmed.fq.gz' $reads'all_r2_trimmed.fq.gz' $reads'all_unpaired.fq.gz' $SCRATCHDIR

assembly='EU1718_contigs_joined_2.fa'
fw='all_r1_trimmed.fq.gz'
rv='all_r2_trimmed.fq.gz'
unpaired='all_unpaired.fq.gz'

base_name='EU1718_bwa_'
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
